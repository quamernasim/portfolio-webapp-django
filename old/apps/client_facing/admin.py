from django.contrib import admin
from .models import BasicInfo, SocialMedia, Projects, Research, Education, Experience, Skills
# Register your models here.

@admin.register(BasicInfo)
class BasicInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'firstname', 'lastname', 'email', 'country_code', 'phone_number', 'city', 'state', 'country', 'zip_code', 'address']
    list_filter = ['id', 'firstname', 'lastname', 'email', 'country_code', 'phone_number', 'city', 'state', 'country', 'zip_code', 'address']
    search_fields = ['id', 'firstname', 'lastname', 'email', 'country_code', 'phone_number', 'city', 'state', 'country', 'zip_code', 'address']
    list_per_page = 100

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['id', 'facebook', 'twitter', 'instagram', 'linkedin', 'github', 'medium', 'stackoverflow', 'whatsapp', 'telegram']
    list_filter = ['id', 'facebook', 'twitter', 'instagram', 'linkedin', 'github', 'medium', 'stackoverflow', 'whatsapp', 'telegram']
    search_fields = ['id', 'facebook', 'twitter', 'instagram', 'linkedin', 'github', 'medium', 'stackoverflow', 'whatsapp', 'telegram']
    list_per_page = 100

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'project_type', 'image', 'link']
    list_filter = ['id', 'title', 'description', 'project_type', 'image', 'link']
    search_fields = ['id', 'title', 'description', 'project_type', 'image', 'link']
    list_per_page = 100

@admin.register(Research)
class ResearchAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'abstract', 'article_type', 'image', 'link']
    list_filter = ['id', 'title', 'abstract', 'article_type', 'image', 'link']
    search_fields = ['id', 'title', 'abstract', 'article_type', 'image', 'link']
    list_per_page = 100

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'degree', 'institution', 'start_year', 'end_year']
    list_filter = ['id', 'degree', 'institution', 'start_year', 'end_year']
    search_fields = ['id', 'degree', 'institution', 'start_year', 'end_year']
    list_per_page = 100

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'company', 'year', 'description']
    list_filter = ['id', 'title', 'company', 'year', 'description']
    search_fields = ['id', 'title', 'company', 'year', 'description']
    list_per_page = 100

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['id', 'skill']
    list_filter = ['id', 'skill']
    search_fields = ['id', 'skill']
    list_per_page = 100



