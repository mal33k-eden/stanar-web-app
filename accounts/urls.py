from django.urls import path
from . import views


urlpatterns=[
    path('bus/register/',views.registerAccount, name='register'),
    path('bus/login/',views.loginAccount, name='login'),
]