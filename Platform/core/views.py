from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Profile, Chat
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import json, time
from django.core import serializers
from datetime import datetime

@login_required(login_url='landing')
def index(request):
    user_profile = Profile.objects.get(user=request.user)

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

    dates = Profile.objects.all()
    dates = dates.exclude(id_user=user_profile.id_user)[:5]
    user_profile.save()

    return render(request, 'index.html', {'user_profile' : user_profile, 'dates' : dates, 
    'date_requests' : date_requests, 'msgs_previews' : msg_previews })

def landing(request): return render(request, 'landing.html')
def terms(request): return render(request, 'terms.html')
def pitch(request): return render(request, 'pitch.html')

@login_required(login_url='landing')
def setup(request):
    user_profile = Profile.objects.get(user=request.user)
    return render(request, 'setup.html', { 'user_profile' : user_profile })
