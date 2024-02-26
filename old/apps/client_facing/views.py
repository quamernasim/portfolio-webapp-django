from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import BasicInfoForm, SocialMediaForm, ProjectsForm, ResearchForm, EducationForm
from .models import BasicInfo, SocialMedia, Projects, Research, Education, Skills, Experience
from django.contrib import messages
from django.core.paginator import Paginator

ROOT_USER = 'quamer'

# Create your views here.

class BasicInfoView(View):
    def get(self, request):
        if str(request.user) == ROOT_USER:
            if BasicInfo.objects.all().count() == 0:
                form = BasicInfoForm()
                return render(request, 'client_facing/info_add.html', locals())
            else:
                basic = BasicInfo.objects.all()
                return render(request, 'client_facing/info.html', locals())
        else:
            return render(request, 'user_facing/home.html', {})
        
    def post(self, request):
        if request.method == 'POST':
            form = BasicInfoForm(request.POST)
            if form.is_valid():
                firstname = form.cleaned_data['firstname']
                lastname = form.cleaned_data['lastname']
                email = form.cleaned_data['email']
                country_code = form.cleaned_data['country_code']
                phone_number = form.cleaned_data['phone_number']
                city = form.cleaned_data['city']
                state = form.cleaned_data['state']
                country = form.cleaned_data['country']
                zip_code = form.cleaned_data['zip_code']
                address = form.cleaned_data['address']

                basic_info = BasicInfo(firstname=firstname, 
                                    lastname=lastname, 
                                    email=email, 
                                    country_code=country_code, 
                                    phone_number=phone_number,
                                    city=city,
                                    state=state,
                                    country=country,
                                    zip_code=zip_code,
                                    address=address)
                basic_info.save()
                
                messages.success(request, 'Your basic information has been saved successfully.')
            else:
                messages.error(request, 'Please correct the error below.')
                messages.error(request, form.errors)

        return redirect('add_basic_info')
    
class SocialMediaView(View):
    def get(self, request):
        if str(request.user) == ROOT_USER:
            if SocialMedia.objects.all().count() == 0:
                form = SocialMediaForm()
                return render(request, 'client_facing/social_media.html', locals())
            else:
                social = SocialMedia.objects.all()
                return render(request, 'client_facing/social_info.html', locals())
        else:
            return render(request, 'user_facing/home.html', {})

    def post(self, request):
        if request.method == 'POST':
            form = SocialMediaForm(request.POST)
            if form.is_valid():
                facebook = form.cleaned_data['facebook']
                twitter = form.cleaned_data['twitter']
                instagram = form.cleaned_data['instagram']
                linkedin = form.cleaned_data['linkedin']
                github = form.cleaned_data['github']
                medium = form.cleaned_data['medium']
                stackoverflow = form.cleaned_data['stackoverflow']
                whatsapp = form.cleaned_data['whatsapp']
                telegram = form.cleaned_data['telegram']

                social_media = SocialMedia(facebook=facebook, 
                                    twitter=twitter, 
                                    instagram=instagram, 
                                    linkedin=linkedin, 
                                    github=github,
                                    medium=medium,
                                    stackoverflow=stackoverflow,
                                    whatsapp=whatsapp,
                                    telegram=telegram)
                social_media.save()
                
                messages.success(request, 'Your social media information has been saved successfully.')
            else:
                messages.error(request, 'Please correct the error below.')
                messages.error(request, form.errors)

        return redirect('social_media')
    
class ProjectView(View):
    def get(self, request):
        if str(request.user) == ROOT_USER:
            form = ProjectsForm()
            return render(request, 'client_facing/add_projects.html', locals())
        else:
            return render(request, 'user_facing/home.html', {})
        
    def post(self, request):
        if request.method == 'POST':
            form = ProjectsForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                project_type = form.cleaned_data['project_type']
                image = form.cleaned_data['image']
                link = form.cleaned_data['link']

                project = Projects(title=title, 
                                    description=description, 
                                    project_type=project_type, 
                                    image=image, 
                                    link=link)
                project.save()
                
                messages.success(request, 'Your project has been saved successfully.')
            else:
                messages.error(request, 'Please correct the error below.')
                messages.error(request, form.errors)

        return redirect('add_project')

class ResearchView(View):
    def get(self, request):
        if str(request.user) == ROOT_USER:
            form = ResearchForm()
            return render(request, 'client_facing/add_research.html', locals())
        else:
            return render(request, 'user_facing/home.html', {})
        
    def post(self, request):
        if request.method == 'POST':
            form = ResearchForm(request.POST, request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                abstract = form.cleaned_data['abstract']
                article_type = form.cleaned_data['article_type']
                image = form.cleaned_data['image']
                link = form.cleaned_data['link']

                research = Research(title=title, 
                                    abstract=abstract, 
                                    article_type=article_type, 
                                    image=image, 
                                    link=link)
                research.save()
                
                messages.success(request, 'Your research has been saved successfully.')
            else:
                messages.error(request, 'Please correct the error below.')
                messages.error(request, form.errors)

        return redirect('add_research')

class ResearchInfoView(View):
    def get(self, request):
        if str(request.user) == ROOT_USER:
            research = Research.objects.all()
            return render(request, 'client_facing/research.html', locals())
        else:
            return render(request, 'user_facing/home.html', {})

class ProjectsInfoView(View):
    def get(self, request):
        if str(request.user) == ROOT_USER:
            projects = Projects.objects.all()
            paginator = Paginator(projects, 3)
            page_num = request.GET.get('page')
            proj = paginator.get_page(page_num)
            total_pages = proj.paginator.num_pages
            total_page_list = [n+1 for n in range(total_pages)]
            current_page = proj.number
            return render(request, 'client_facing/projects.html', locals())
        else:
            return render(request, 'user_facing/home.html', {})
        
class UpdateResearch(View):
    def get(self, request, id):
        if str(request.user) == ROOT_USER:
            research = Research.objects.get(id=id)
            form = ResearchForm(instance=research)
            return render(request, 'client_facing/update_research.html', locals())
        else:
            return render(request, 'user_facing/home.html', {})
    
    def post(self, request, id):
        if request.method == 'POST':
            research = Research.objects.get(id=id)
            form = ResearchForm(request.POST, request.FILES, instance=research)
            if form.is_valid():
                title = form.cleaned_data['title']
                abstract = form.cleaned_data['abstract']
                article_type = form.cleaned_data['article_type']
                image = form.cleaned_data['image']
                link = form.cleaned_data['link']

                research.title = title
                research.abstract = abstract
                research.article_type = article_type
                research.image = image
                research.link = link
                research.save()
                
                messages.success(request, 'Your research has been updated successfully.')
            else:
                messages.error(request, 'Please correct the error below.')
                messages.error(request, form.errors)

        return redirect('research')
    
    def delete(self, request, id):
        if request.method == 'DELETE':
            research = Research.objects.get(id=id)
            research.delete()
            messages.success(request, 'Your research has been deleted successfully.')

        return redirect('research')