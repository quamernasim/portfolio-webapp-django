from django.contrib import admin
from django.urls import path, include
from ..views import basic
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('profile_update/', basic.BasicInfoView.as_view(), name='basic_info_api'),
    path('social_update/', basic.SocialMediaView.as_view(), name='scoial_info_api'),
    path('education_update/', basic.EducationView.as_view(), name='education_info_api'),

]