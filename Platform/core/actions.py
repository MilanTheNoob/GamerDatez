from datetime import date
from time import sleep
from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse, JsonResponse
from .models import Profile, Chat
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import os, json
from django.contrib.sessions.models import Session
import random
import base64

#MAJOR FUCKING BANDAID TO GET THIS WORKING BTW
os.add_dll_directory(r"C:\gtk3\bin")
import py_avataaars as pa

def login(request):
    user = auth.authenticate(username=request.POST['lusername'], password=request.POST['lpassword'])
    if user is not None:
        auth.login(request, user)
        return JsonResponse({ 'response' : True })
    else:
        return JsonResponse({ 'response' : False })

def signup(request):
    username = request.POST['username']
    if User.objects.filter(username=username).exists() is not True:
        password = ''
 
        for _ in range(10):
            random_int = random.randint(0, 255)
            password += (chr(random_int))
        
        user = User.objects.create_user(username=username, password=password)
        user.save()

        user_login = auth.authenticate(username=username, password=password)
        auth.login(request, user_login)

        user_model = User.objects.get(username=username)
        new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
        new_profile.save()

        return JsonResponse({ 'response' : True })
    else:
        return JsonResponse({ 'response' : False })

@login_required(login_url='landing')
def logout(request):
    auth.logout(request)
    return JsonResponse({ 'response' : True })

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

    return JsonResponse({ 'response' : True })

@login_required(login_url='landing')
def finish_setup(request):
    user_profile = Profile.objects.get(user=request.user)
    
    user_profile.first_name = request.POST.get('first_name')
    user_profile.last_name = request.POST.get('last_name')
    user_profile.sex = request.POST.get('sex')
    user_profile.preference = request.POST.get('preference')
    user_profile.bio = request.POST.get('bio')
    user_profile.age = request.POST.get('age')
    user_profile.birth_date = request.POST.get('birth_date')
    user_profile.fav_game = request.POST.get('fav_game_1')
    user_profile.sec_fav_game = request.POST.get('fav_game_2')
    user_profile.third_fav_game = request.POST.get('fav_game_3')

    user_profile.save()
    return JsonResponse({ 'response' : True })

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
    online = None

    msgs = json.loads(messages.messages)
    chat_users = json.loads(messages.users)

    user_profile.messages = "[]"
    user_profile.accepting_messages = str(int(messages.id))
    user_profile.save()
            
    for cu in chat_users:
        cu = int(cu.strip('b').strip('e'))
        if cu != user_profile.id_user:
            mu = Profile.objects.get(id_user=cu)
            person = mu.first_name
            img = mu.profileimg.url
            online_bool = mu.user.is_authenticated
            if online_bool: online = 'Logged in'
            else: online = 'Logged out'

    return JsonResponse({ 'person' : person, 'doing' : online, 'msgs' : msgs, 'img' : img })

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
        mu = Profile.objects.get(id_user=int(cu.strip('b').strip('e')))

        if mu.id_user != user_profile.id_user and mu.accepting_messages == str(int(messages.id)):
            dat = json.loads(mu.messages)
            dat.append(msg)
            mu.messages = json.dumps(dat)

            mu.save()

    return JsonResponse({ 'msg' : msg })

@login_required(login_url='landing')
def update_values(request):
    user_profile = Profile.objects.get(user=request.user)
    
    if user_profile.messages != "[]":
        dat = json.loads(user_profile.messages)

        user_profile.messages = "[]"
        user_profile.save()

        return JsonResponse({ 'success' : True, 'value' : dat })
    else:
        return JsonResponse({ 'success' : False }) 

def check_username(request):
    value = request.POST['value']
    print(value)
    return JsonResponse({ 'response' : User.objects.filter(username__iexact=value).exists() })

def preview_avatar(request):
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

    test = base64.encodebytes(avatar.render_png()).decode('utf-8')
    return JsonResponse({ 'response' : True, 'image' : test})