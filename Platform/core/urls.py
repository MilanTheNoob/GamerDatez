from django.urls import path
from . import views
from . import actions

urlpatterns = [
    path('', views.index, name='index'),
    path('landing', views.landing, name='landing'),
    path('logout', views.logout, name='logout'),
    path('terms', views.terms, name='terms'),
    path('info', views.pitch, name='pitch'),
    path('setup', views.setup, name='setup'),

    path('actions/submit-avatar', actions.submit_avatar, name='submit-avatar'),
    path('actions/finish-setup', actions.finish_setup, name='finish-setup'),
    path('actions/like-date', actions.like_date, name='like-date'),
    path('actions/accept-date', actions.date_accept, name='accept-date'),
    path('actions/deny-date', actions.date_deny, name='deny-date'),
    path('actions/load-messages', actions.load_messages, name='load-messages'),
    path('actions/submit-message', actions.submit_message, name='submit-message'),
    path('actions/update-messages', actions.update_messages, name='update-messages'),
]
