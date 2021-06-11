from django.shortcuts import render

# Create your views here.
from todos_app.forms_workshop.user_form import UserForm


def post_show_form_data(request):
    form = UserForm(request.POST)
    if form.is_valid():
        fields = ['name', 'age', 'email', 'password', 'text']
        [print(field, form.cleaned_data[field]) for field in fields]
    else:
        print(form.errors)


def get_show_form_data(request):
    context = {
        'form': UserForm(),
    }
    return render(request, 'forms_workshop/form.html', context)


def show_form_data(request):
    if request.method == 'POST':
        return post_show_form_data(request)
    else:
        return get_show_form_data(request)
