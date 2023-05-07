from django.contrib import admin
from .models.basic import BasicInfo, SocialMedia, Education
from .models.project import Project
from .models.research import Research
from .models.work import Experience, Skill
from .models.auth import AuthUser

# Register your models here.
# admin.site.register(BasicInfo)
admin.site.register(SocialMedia)
admin.site.register(Project)
admin.site.register(Research)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
# admin.site.register(AuthUser)

@admin.register(BasicInfo)
class BasicInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'firstname', 'lastname', 'email', 'country_code', 'phone_number', 'city', 'state', 'country', 'zip_code', 'address')

# @admin.register(SocialMedia)
# class SocialMediaAdmin(admin.ModelAdmin):
#     list_display = ('basic_info', 'facebook', 'twitter', 'instagram', 'linkedin', 'github', 'medium', 'stackoverflow', 'whatsapp', 'telegram')

# @admin.register(Project)
# class ProjectAdmin(admin.ModelAdmin):
#     list_display = ('user', 'title', 'description', 'link', 'start_date', 'end_date')

# @admin.register(Research)
# class ResearchAdmin(admin.ModelAdmin):
#     list_display = ('user', 'title', 'description', 'link', 'start_date', 'end_date')

# @admin.register(Education)
# class EducationAdmin(admin.ModelAdmin):
#     list_display = ('degree', 'institution', 'start_year', 'end_year', 'user')

# @admin.register(Experience)
# class ExperienceAdmin(admin.ModelAdmin):
#     list_display = ('title', 'company', 'start_date', 'end_date', 'user')

# @admin.register(Skill)
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ('title', 'user')

@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'password')