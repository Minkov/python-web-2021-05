from django.shortcuts import render

from django101.cities.models import Person


def index(req):
    context = {
        'name': 'Doncho',
        'people': Person.objects.all(),
    }

    return render(req, 'index.html', context)


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
