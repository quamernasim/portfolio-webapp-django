from django.db import models

# Create your models here.

PROJECT_TYPE_CHOICES = (
    ("Machine Learning", "Machine Learning"),
    ("Deep Learning", "Deep Learning"),
    ("Django", "Django")
    )

ARTICLE_TYPE_CHOICES = (
    ("Publications", "Publications"),
    ("Conferences", "Conferences"),
    ("PrePrints", "PrePrints")
    )

# Create your models here.
class BasicInfo(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    country_code = models.IntegerField()
    phone_number = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    address = models.CharField(max_length=100)

class SocialMedia(models.Model):
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkedin = models.URLField()
    github = models.URLField()
    medium = models.URLField(blank=True)
    stackoverflow = models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    telegram = models.URLField(blank=True)

class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_type = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=100)
    image = models.ImageField(upload_to='project/', blank=True)
    link = models.URLField(blank=True)

class Research(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    article_type = models.CharField(choices=ARTICLE_TYPE_CHOICES, max_length=100)
    author_names = models.CharField(max_length=200, default="")
    image = models.ImageField(upload_to='research/', blank=True)
    link = models.URLField(blank=True)

class Education(models.Model):
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=100)
    start_year = models.IntegerField()
    end_year = models.IntegerField()

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()

class Skills(models.Model):
    skill = models.CharField(max_length=100)
    level = models.IntegerField()

