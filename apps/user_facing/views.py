from django.shortcuts import render, redirect
from django.views.generic import View
# from .forms import BasicInfoForm, SocialMediaForm, ProjectsForm
from apps.client_facing.models import BasicInfo, SocialMedia, Projects, Research, Education, Skills, Experience
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'user_facing/home.html', {})

class ProjectInfoView(View):
    def get(self, request):
        projects = Projects.objects.all()
        return render(request, 'user_facing/projects.html', {'projects': projects})

class ResearchInfoView(View):
    def get(self, request):
        if request.path=="/publications_info/":
            researches = Research.objects.filter(article_type='Publications')
            return render(request, 'user_facing/publications.html', {'researches': researches})
        
        elif request.path=="/conferences_info/":
            researches = Research.objects.filter(article_type='Conferences')
            return render(request, 'user_facing/conferences.html', {'researches': researches})
        
        elif request.path=="/preprints_info/":
            researches = Research.objects.filter(article_type='PrePrints')
            return render(request, 'user_facing/preprints.html', {'researches': researches})
        
        else:
            return redirect('/')
