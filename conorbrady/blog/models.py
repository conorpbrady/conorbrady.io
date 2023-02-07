from django.db import models

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=32)

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    labels = models.ManyToManyField('Label')
    pub_date = models.DateTimeField()
