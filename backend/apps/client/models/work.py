from django.db import models
from .basic import BasicInfo
# Create your models here.


class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Skill(models.Model):
    skill = models.CharField(max_length=100)
    level = models.IntegerField()
    user = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill

