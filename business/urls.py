from django.urls import path
from . import views


urlpatterns=[
    # path('',views.dashboard, name='bus.dashboard'),
    path('dashboard/',views.dashboard, name='bus.dashboard'),
    path('profile/',views.profile, name='bus.profile'),
    path('options/',views.options, name='bus.options'),
    path('options/<str:type>/',views.options, name='bus.options'),
    path('photos/',views.photos, name='bus.photos'),
    path('services/',views.services, name='bus.services'),
    path('services/<int:pk>/update',views.updateService, name='bus.services.update'),
    path('services/<int:pk>/delete',views.deleteService, name='bus.services.delete'),
    path('staff',views.staff, name='bus.staff'),
    path('staff/<int:pk>/update',views.updateStaff, name='bus.staff.update'),
    path('staff/<int:pk>/delete',views.deleteStaff, name='bus.staff.delete'),
]