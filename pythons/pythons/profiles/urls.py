from django.urls import path

from pythons.profiles.views import profile_details

urlpatterns = (
    path('', profile_details, name='profile details'),
)

import pythons.profiles.signals
