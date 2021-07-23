from django.db import models


class Python(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.ImageField()
    slug = models.SlugField()
