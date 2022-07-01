from datetime import date
from time import sleep
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, JsonResponse
from .models import Profile, Chat
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import os, json
from django.contrib.sessions.models import Session

#MAJOR FUCKING BANDAID TO GET THIS WORKING BTW
os.add_dll_directory(r"C:\gtk3\bin")
import py_avataaars as pa

@login_required(login_url='landing')
def submit_avatar(request):
    if request.method == 'POST':
        user_profile = Profile.objects.get(user=request.user)
        avatar = pa.PyAvataaar(
        style = pa.AvatarStyle.TRANSPARENT,
        skin_color = pa.SkinColor[request.POST.get('pp_skin')],
        hair_color = pa.HairColor[request.POST.get('pp_hair_color')],
        facial_hair_type = pa.FacialHairType[request.POST.get('pp_facial')],
        facial_hair_color = pa.HairColor[request.POST.get('pp_hair_color')],
        top_type = pa.TopType[request.POST.get('pp_top')],
        hat_color = pa.Color[request.POST.get('pp_hair_color')],
        mouth_type = pa.MouthType[request.POST.get('pp_mouth')],
        eye_type = pa.EyesType[request.POST.get('pp_eyes')],
        accessories_type = pa.AccessoriesType[request.POST.get('pp_glasses')],
        clothe_type = pa.ClotheType[request.POST.get('pp_clothes')],
        clothe_color = pa.Color[request.POST.get('pp_clothes_color')],
        clothe_graphic_type = pa.ClotheGraphicType[request.POST.get('pp_clothes_graphics')]
        )

        avatar.render_png_file('media/profile_images/' + user_profile.user.username + '.png')
        user_profile.profileimg.name = 'profile_images/' + user_profile.user.username + '.png'
        user_profile.save()

    return redirect('setup')

@login_required(login_url='landing')
def finish_setup(request):
    if request.method == 'POST':
        try:
            user_profile = Profile.objects.get(user=request.user)
        
            user_profile.first_name = request.POST.get('first_name')
            user_profile.last_name = request.POST.get('last_name')
            user_profile.sex = request.POST.get('sex')
            user_profile.preference = request.POST.get('preference')
            user_profile.bio = request.POST.get('bio')
            user_profile.age = request.POST.get('age')
            user_profile.birth_date = request.POST.get('birth_date')
            user_profile.country = request.POST.get('country')
            user_profile.fav_game = request.POST.get('fav_game_1')
            user_profile.sec_fav_game = request.POST.get('fav_game_2')
            user_profile.third_fav_game = request.POST.get('fav_game_3')

            user_profile.save()
            return redirect('/')
        except:
            return redirect('setup')
    else:
        return redirect('setup')

@login_required(login_url='landing')
def like_date(request):
    response = None
    date_list = None

    new_date = int(request.POST['value'])
    user_profile = Profile.objects.get(id_user=new_date)

    try: date_list = json.loads(user_profile.date_requests)
    except: date_list = []

    if new_date not in date_list:
        date_list.append(Profile.objects.get(user=request.user).id_user)

        user_profile.date_requests = json.dumps(date_list)
        user_profile.save()

        response = { 'success' : True }
    else: response = { 'success' : False }

    return JsonResponse(response)
        
@login_required(login_url='landing')
def date_accept(request):
    user_profile = Profile.objects.get(user=request.user)
    did = int(request.POST['value'])
    dr = json.loads(user_profile.date_requests)

    Chat.objects.create(users=json.dumps([ 'b' + str(user_profile.id_user) + 'e', 'b' + str(did) + 'e' ]),
    messages=json.dumps([ "<b>" + str(user_profile.first_name) + "</b> Hello there!" ]), admin=user_profile.id_user)

    if did in dr: 
        dr.remove(did)
        user_profile.date_requests = json.dumps(dr)
        user_profile.save()
    return JsonResponse({ 'success' : True })

@login_required(login_url='landing')
def date_deny(request):
    user_profile = Profile.objects.get(user=request.user)
    dr = json.loads(user_profile.date_requests)

    did = int(request.POST['value'])
    if did in dr: dr.remove(did)

@login_required(login_url='landing')
def load_messages(request):
    user_profile = Profile.objects.get(user=request.user)
    messages = Chat.objects.get(id=request.POST['value'])
    person = None
    img = None

    msgs = json.loads(messages.messages)
    chat_users = json.loads(messages.users)

    user_profile.accepting_messages = messages.id
    user_profile.save()
            
    for cu in chat_users:
        cu = int(cu.strip('b').strip('e'))
        if cu != user_profile.id_user:
            mu = Profile.objects.get(id_user=cu)
            person = mu.first_name
            img = mu.profileimg.url

    return JsonResponse({ 'person' : person, 'doing' : 'Online', 'msgs' : msgs, 'img' : img })

@login_required(login_url='landing')
def submit_message(request):
    user_profile = Profile.objects.get(user=request.user)
    messages = Chat.objects.get(id=request.POST['chatId'])
    msg = '<b>' + user_profile.first_name + '</b> ' + request.POST['msg']
    chat_users = json.loads(messages.users)

    msgs = json.loads(messages.messages)
    msgs.append(msg)
    messages.messages = json.dumps(msgs)
    messages.save()

    for cu in chat_users:
        cu = int(cu.strip('b').strip('e'))
        if cu != user_profile.id_user:
            mu = Profile.objects.get(id_user=cu)
            if mu.user.is_authenticated and mu.accepting_messages == messages.id:
                dat = json.loads(mu.messages)
                dat.append(msg)
                mu.messages = json.dumps(dat)

                mu.save()

    return JsonResponse({ 'msg' : msg })

@login_required(login_url='landing')
async def update_messages(request):
    user_profile = Profile.objects.get(user=request.user)
    i = 0

    while i < 16:
        if user_profile.messages != "[]":
            dat = json.loads(user_profile.messages)

            user_profile.messages = "[]"
            user_profile.save()

            return JsonResponse({ 'value' : dat })

        user_profile.refresh_from_db()

        i += 1
        sleep(4)

