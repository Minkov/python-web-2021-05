from django.contrib import admin

from phones_media_files.phones.models import Phone, PhoneImage


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(PhoneImage)
class PhoneImageAdmin(admin.ModelAdmin):
    pass
