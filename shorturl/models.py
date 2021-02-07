from django.db import models

# Create your models here

class Urls(models.Model):
    link = models.CharField(max_length=500000)
    linkid = models.CharField(max_length=10)