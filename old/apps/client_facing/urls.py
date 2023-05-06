from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.BasicInfoView.as_view(), name='add_basic_info'),
    path('social_media/', views.SocialMediaView.as_view(), name='social_media'),
    path('add_project/', views.ProjectView.as_view(), name='add_project'),
    path('projects/', views.ProjectsInfoView.as_view(), name='projects'),
    path('add_research/', views.ResearchView.as_view(), name='add_research'),
    path('research/', views.ResearchInfoView.as_view(), name='research'),
    path('update_research/<int:id>/', views.UpdateResearch.as_view(), name='update_research'),
    path('delete_research/<int:id>/', views.UpdateResearch.as_view(), name='delete_research'),

    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

]