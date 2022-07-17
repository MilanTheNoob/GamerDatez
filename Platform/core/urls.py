from django.urls import path
from . import views
from . import actions

urlpatterns = [
    path('', views.index, name='index'),
    path('landing', views.landing, name='landing'),
    path('terms', views.terms, name='terms'),
    path('info', views.pitch, name='pitch'),
    path('setup', views.setup, name='setup'),

    path('actions/login', actions.login, name='login'),
    path('actions/signup', actions.signup, name='signup'),
    path('actions/logout', actions.logout, name='logout'),
    path('actions/submit-avatar', actions.submit_avatar, name='submit-avatar'),
    path('actions/finish-setup', actions.finish_setup, name='finish-setup'),
    path('actions/like-date', actions.like_date, name='like-date'),
    path('actions/accept-date', actions.date_accept, name='accept-date'),
    path('actions/deny-date', actions.date_deny, name='deny-date'),
    path('actions/load-messages', actions.load_messages, name='load-messages'),
    path('actions/submit-message', actions.submit_message, name='submit-message'),
    path('actions/update-values', actions.update_values, name='update-values'),
    path('actions/check-username', actions.check_username, name='check-username'),
    path('actions/preview-avatar', actions.preview_avatar, name='preview-avatar'),
]
