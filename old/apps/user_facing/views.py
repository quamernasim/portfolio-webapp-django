from django.shortcuts import render, redirect
from django.views.generic import View
# from .forms import BasicInfoForm, SocialMediaForm, ProjectsForm
from apps.client_facing.models import BasicInfo, SocialMedia, Projects, Research, Education, Skills, Experience
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    return render(request, 'user_facing/home.html', {})

class ProjectInfoView(View):
    def get(self, request):
        projects_ = Projects.objects.all()
        paginator = Paginator(projects_, 3)
        page_num = request.GET.get('page')
        projectss = paginator.get_page(page_num)
        total_pages = projectss.paginator.num_pages
        total_page_list = [n+1 for n in range(total_pages)]
        current_page = projectss.number
        return render(request, 'user_facing/projects.html', locals())

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
