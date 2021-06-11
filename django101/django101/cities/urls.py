# cities.urls
from django.urls import path

from django.views.generic import TemplateView

from django101.cities.views import index, list_phones, test_index, create_person, show_forms_demo

urlpatterns = [
    path('', index),  # /'cities/' + '' = '/cities/'
    path('create/', create_person, name='create person'),
    path('test/', test_index),
    path('phones/', list_phones),  # /'cities/' + 'phones/' = '/cities/phones/'
    path('phones2/', TemplateView.as_view(template_name='cities/phones.html')),  # for the next course
    path('forms/', show_forms_demo),
]
