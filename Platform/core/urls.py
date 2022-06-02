from django.urls import path
from . import views
from . import actions

urlpatterns = [
    path('', views.index, name='index'),
    path('landing', views.landing, name='landing'),
    path('logout', views.logout, name='logout'),
    path('terms', views.terms, name='terms'),
    path('pitch', views.pitch, name='pitch'),
    path('setup', views.setup, name='setup'),

    path('actions/create-post', actions.create_post, name='create-post'),
    path('actions/submit-avatar', actions.submit_avatar, name='submit-avatar'),
    path('actions/finish-setup', actions.create_post, name='finish-setup'),
]
