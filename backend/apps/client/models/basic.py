from django.db import models
from .auth import AuthUser
# Create your models here.

# Create your models here.
class BasicInfo(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, related_name='basic_info')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50 ,blank=True)
    country_code = models.IntegerField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class SocialMedia(models.Model):
    basic_info = models.OneToOneField(BasicInfo, on_delete=models.CASCADE, related_name='social_media')
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField()
    github = models.URLField()
    medium = models.URLField(blank=True)
    stackoverflow = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    telegram = models.URLField(blank=True)

    def __str__(self):
        return self.linkedin

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    user = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.degree

