from django.db import models
from .basic import BasicInfo

# Create your models here.

PROJECT_TYPE_CHOICES = (
    ("Machine Learning", "Machine Learning"),
    ("Deep Learning", "Deep Learning"),
    ("Django", "Django")
    )

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    project_type = models.CharField(choices=PROJECT_TYPE_CHOICES, max_length=100)
    image = models.ImageField(upload_to='project/', blank=True)
    link = models.URLField(blank=True)
    user = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

