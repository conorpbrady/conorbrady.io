from django.db import models

# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    labels = models.ManyToManyField('Label', blank=True)
    pub_date = models.DateTimeField()
    slug = models.CharField(max_length=255)
    modified_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.slug
