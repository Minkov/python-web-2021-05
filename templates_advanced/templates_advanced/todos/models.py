from django.db import models


class Todo(models.Model):
    text = models.CharField(
        max_length=30,
    )

    is_done = models.BooleanField(
        default=False,
    )
