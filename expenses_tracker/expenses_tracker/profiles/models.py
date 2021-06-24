from django.db import models


class Profile(models.Model):
    first_name = models.CharField(
        max_length=15,
    )

    last_name = models.CharField(
        max_length=15,
    )
    budget = models.IntegerField()

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
