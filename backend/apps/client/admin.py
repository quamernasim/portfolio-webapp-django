from django.contrib import admin
from .models.basic import BasicInfo, SocialMedia, Education
from .models.project import Project
from .models.research import Research
from .models.work import Experience, Skill
from .models.auth import AuthUser

# Register your models here.
admin.site.register(BasicInfo)
admin.site.register(SocialMedia)
admin.site.register(Project)
admin.site.register(Research)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(Skill)
admin.site.register(AuthUser)