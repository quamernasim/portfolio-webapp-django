from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.basic_info, name='basic_info'),
    path('info_add/', views.info_add, name='info_add'),
    path('info_update/', views.info_update, name='info_update'),
    path('delete_info/', views.delete_info, name='delete_info'),

    path('social_media/', views.social_media, name='social_media'),
    path('social_media_add/', views.social_media_add, name='social_media_add'),
    path('social_media_update/', views.social_media_update, name='social_media_update'),
    path('delete_social_media/', views.delete_social_media, name='delete_social_media'),


    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register')
]