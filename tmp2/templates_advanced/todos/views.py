from django.shortcuts import render, redirect

from templates_advanced.todos.forms import TodoForm
from templates_advanced.todos.models import Todo


def list_todos(request):
    context = {
        'todos': Todo.objects.all(),
        'page_name': 'list_todos',
    }

    return render(request, 'todos/list_todos.html', context)


def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list todos')
    else:
        form = TodoForm()

    context = {
        'form': form,
        'page_name': 'create_todo',
    }

    return render(request, 'todos/create_todo.html', context)
