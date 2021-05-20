from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin2/', admin.site.urls),
    path('cities/', include('django101.cities.urls')),
    path('', include('django101.people.urls')),

    # path('cities/', index),
    # path('cities/phones', list_phones)
]
