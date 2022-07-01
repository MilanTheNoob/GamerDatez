from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Chat
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import json
from django.core import serializers

@login_required(login_url='landing')
def index(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        bio = request.POST.get('account-bio')
        image = None
        if request.FILES.get('account-image') == None:
            image = user_profile.profileimg
        else:
            image = request.FILES.get('account-image')

        user_profile.profileimg = image
        user_profile.bio = bio
        user_profile.save()
    else:
        skey = request.session.session_key
        dr_ids = json.loads(user_profile.date_requests)

        dates = None
        date_requests = []

        mpQuery = Chat.objects.filter(users__contains='b' + str(user_profile.id_user) + 'e')
        msg_previews = []

        for chat in mpQuery:
            msg_preview = { 'icon' : None, 'name' : '', 'preview' : 'test', 'id' : str(chat.id) }
            chat_users = json.loads(chat.users)
            
            for cu in chat_users:
                cu = int(cu.strip('b').strip('e'))
                if cu != user_profile.id_user:
                    mu = Profile.objects.get(id_user=cu)

                    msg_preview['icon'] = mu.profileimg
                    msg_preview['name'] = mu.first_name

            msg_previews.append(msg_preview)

        for dr_id in dr_ids: date_requests.append(Profile.objects.get(user_id=dr_id))

        try: dates = Profile.objects.filter(pk__in=map(lambda o: o.object.pk, serializers.deserialize("json", request.session[skey]),))
        except:
            dates = Profile.objects.all()[:5]
            request.session[skey] = serializers.serialize("json", dates)

        user_profile.save()

    return render(request, 'index.html', {'user_profile' : user_profile, 'dates' : dates, 
    'date_requests' : date_requests, 'msgs_previews' : msg_previews })

def landing(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        lusername = request.POST.get('lusername')
        lpassword = request.POST.get('lpassword')

        if username is not None:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'That email already been used bro')
                return redirect('landing')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Someone stole your name mate!')
                return redirect('landing')
            elif '@' not in email:
                messages.info(request, 'Now wait a minute, that email aint right')
                return redirect('landing')
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()

                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()

                return redirect('setup')
        elif lusername is not None:
            user = auth.authenticate(username=lusername, password=lpassword)

            if user is not None:
                auth.login(request, user)
                return redirect('/')
            else:
                messages.info(request, "Please reinput your info or create an account.")
                return redirect('landing')

    return render(request, 'landing.html')

def terms(request):
    return render(request, 'terms.html')

def pitch(request):
    return render(request, 'pitch.html')

def logout(request):
    auth.logout(request)
    return redirect('landing')

@login_required(login_url='landing')
def setup(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'setup.html', { 'game_options' : Profile.games, 'user_profile' : user_profile })
