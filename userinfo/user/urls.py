from django.urls import path
from .views import get_User_info, show_user_info

app_name = 'user'

urlpatterns = [
    path('', get_User_info, name='user-form'),
    path('info/', show_user_info, name='user-info')
]
