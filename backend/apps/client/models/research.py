from django.db import models
from .basic import BasicInfo

# Create your models here.

ARTICLE_TYPE_CHOICES = (
    ("Publications", "Publications"),
    ("Conferences", "Conferences"),
    ("PrePrints", "PrePrints")
    )

class Research(models.Model):
    title = models.CharField(max_length=200)
    abstract = models.TextField()
    article_type = models.CharField(choices=ARTICLE_TYPE_CHOICES, max_length=100)
    author_names = models.CharField(max_length=200)
    image = models.ImageField(upload_to='research/', blank=True)
    link = models.URLField(blank=True)
    user = models.ForeignKey(BasicInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

