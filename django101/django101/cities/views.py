from django.http import HttpResponse
from django.shortcuts import render, redirect

from django101.cities.models import Person


def show_forms_demo(request):
    return render(request, 'forms_demo.html')

def index(req):
    context = {
        'name': 'Doncho',
        'people': Person.objects.all(),
    }

    return render(req, 'index.html', context)


def create_person(req):
    Person(
        name='Pesho',
        age=11,
        home_town='Sofia',
    ).save()

    return redirect('/cities')


def test_index(req):
    return HttpResponse(
        '{"name": "Doncho"}',
        content_type='application/json')


def list_phones(request):
    context = {
        'phones': [
            {
                'name': 'Galaxy S5000',
                'quantity': 3,
            },
            {
                'name': 'Xiaomi Redmi 5',
                'quantity': 0,
            },
            {
                'name': 'iPhone 12',
                'quantity': 4,
            },
        ]
    }

    context['message'] = 'Phones list'
    return render(request, 'cities/phones.html', context)
