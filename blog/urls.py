from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('uzbekistan/', views.uzbekistan, name='uzbekistan'),
    path('time/', views.current_time, name='time'),
    path('device/', views.device, name='device'),
]
