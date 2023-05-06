from django.contrib import admin
from django.urls import path, include
from ..views import basic
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile_update/', basic.BasicInfoView.as_view(), name='basic_info_api'),
    # path('', basic.basic_info, name='basic_info'),
    # path('social_media/', views.SocialMediaView.as_view(), name='social_media'),

    # path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

]