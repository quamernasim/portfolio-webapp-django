from django.contrib import admin
from django.urls import path, include
from .views import basic_info
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', basic_info, name='basic_info'),

]