from django.contrib import admin
from .models.basic import BasicInfo, SocialMedia, Education
from .models.project import Project
from .models.research import Research
from .models.work import Experience, Skill
from .models.auth import AuthUser

# Register your models here.
# admin.site.register(BasicInfo)
# admin.site.register(SocialMedia)
admin.site.register(Project)
admin.site.register(Research)
# admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
# admin.site.register(AuthUser)

@admin.register(BasicInfo)
class BasicInfoAdmin(admin.ModelAdmin):
    list_display = ['__str__'] + [field.name for field in BasicInfo._meta.fields]

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['__str__'] + [field.name for field in SocialMedia._meta.fields]

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['__str__'] + [field.name for field in Education._meta.fields]
    
@admin.register(AuthUser)
class AuthUserAdmin(admin.ModelAdmin):
    list_display = ['__str__'] + [field.name for field in AuthUser._meta.fields]
