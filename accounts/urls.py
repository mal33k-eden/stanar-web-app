from django.urls import path
from . import views


urlpatterns=[
    path('bus/register/',views.registerAccount, name='register'),
    path('bus/login/',views.loginAccount, name='login'),
    path('bus/dashboard/',views.dashboard, name='bus.dashboard'),
    path('bus/profile/',views.dashboard, name='bus.profile'),
    path('bus/staff/',views.dashboard, name='bus.staff'),
    path('bus/staff/add',views.dashboard, name='bus.staff.add'),
    path('bus/staff/delete',views.dashboard, name='bus.staff.del')
]