from django.db import models


class Phone(models.Model):
    manufacturer = models.CharField(
        max_length=30,
    )
    model = models.CharField(
        max_length=15,
    )


class PhoneImage(models.Model):
    image = models.ImageField(
        upload_to='phones',
    )
    is_selected = models.BooleanField(
        default=False,
    )
    phone = models.ForeignKey(Phone, on_delete=models.CASCADE)
