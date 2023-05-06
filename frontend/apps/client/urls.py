from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.basic_info, name='basic_info'),
    path('info_add/', views.info_add, name='info_add'),
    path('info_update/', views.info_update, name='info_update'),
    path('delete_info/', views.delete_info, name='delete_info'),
]