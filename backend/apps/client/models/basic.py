from django.db import models
from .auth import AuthUser
# Create your models here.

# Create your models here.
class BasicInfo(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, related_name='basic_info')
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50 ,blank=True)
    country_code = models.IntegerField()
    phone_number = models.BigIntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.firstname

class SocialMedia(models.Model):
    user = models.OneToOneField(AuthUser, on_delete=models.CASCADE, related_name='social_info', default='')
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
    user = models.ForeignKey(AuthUser, on_delete=models.CASCADE, default='')
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    year = models.IntegerField(default=0)
    cgpa = models.FloatField(default=0)

    def __str__(self):
        return self.degree

