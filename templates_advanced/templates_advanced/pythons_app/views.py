from django.shortcuts import render, redirect
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
def index(req):
    pythons = Python.objects.all()
    return render(req, 'index.html', {'pythons': pythons})


def create(req):
    if req.method == 'GET':
        form = PythonCreateForm()
        return render(req, 'create.html', {'form': form})
    else:
        data = req.POST
        form = PythonCreateForm(data)
        print(form)
        if form.is_valid():
            python = form.save()
            python.save()
            return redirect('index')
