from django.shortcuts import render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile, Post
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
import os

#MAJOR FUCKING BANDAID TO GET THIS WORKING BTW
os.add_dll_directory(r"C:\gtk3\bin")
import py_avataaars as pa

@login_required(login_url='landing')
def create_post(request):
    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('post-image')
        caption = request.POST.get('post-caption')

        new_post = Post.objects.create(user=user, image=image, caption=caption)
        new_post.save()

    return redirect('/')

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
        user_profile.profileimg.name = 'profile_images/' + user_profile.user.username + '.png';
        user_profile.save()

    return redirect('setup')
