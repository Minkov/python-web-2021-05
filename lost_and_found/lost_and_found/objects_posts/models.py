from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models

from lost_and_found.objects_posts.validators import validate_max_value


class Object(models.Model):
    name = models.CharField(
        max_length=10
    )
    image = models.URLField()
    width = models.IntegerField(
        validators=(
            validate_max_value(600),
            MinValueValidator(3),
        )
    )
    height = models.IntegerField()
    weight = models.FloatField()


class Post(models.Model):
    title = models.CharField(
        max_length=30
    )
    description = models.TextField(
        max_length=500
    )
    author_name = models.CharField(
        max_length=10
    )
    author_phone = models.CharField(
        max_length=10
    )
    found = models.BooleanField(
        default=False
    )
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
