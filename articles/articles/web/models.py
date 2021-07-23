from django.db import models


class Source(models.Model):
    name = models.CharField(
        max_length=50,
    )
    url = models.URLField(
        max_length=200,
    )

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(
        max_length=100,
    )
    description = models.TextField()
    image_url = models.URLField(
        max_length=200,
    )

    source = models.ForeignKey(Source, on_delete=models.CASCADE)
