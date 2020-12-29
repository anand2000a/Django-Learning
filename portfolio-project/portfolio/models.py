from django.db import models
from django.db.models.base import ModelState

class Project(models.Model):
    title = models.CharField(max_length=100,blank=True)
    description=models.CharField(max_length=200)
    image = models.ImageField(upload_to='portfolio/images/')
    url=models.URLField(blank=True)