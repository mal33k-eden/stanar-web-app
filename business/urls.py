from django.urls import path
from . import views


urlpatterns=[
    # path('',views.dashboard, name='bus.dashboard'),
    path('dashboard/',views.dashboard, name='bus.dashboard'),
    path('profile/',views.profile, name='bus.profile'),
    path('services/',views.services, name='bus.services'),
    path('staff/add',views.dashboard, name='bus.staff.add'),
    path('staff/delete',views.dashboard, name='bus.staff.del')
]