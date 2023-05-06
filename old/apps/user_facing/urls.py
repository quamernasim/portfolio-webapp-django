from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('projects_info/', views.ProjectInfoView.as_view(), name='projects_info'),
    # path('projects_info/', views.projInfo, name='projects_info'),
    path('publications_info/', views.ResearchInfoView.as_view(), name='publications_info'),
    path('conferences_info/', views.ResearchInfoView.as_view(), name='conferences_info'),
    path('preprints_info/', views.ResearchInfoView.as_view(), name='preprints_info'),
]