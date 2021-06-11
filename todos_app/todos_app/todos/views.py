from django.shortcuts import render, redirect

from todos_app.todos.forms import CreateTodoForm, UpdateTodoForm

#
# def index(request):
#     context = {
#         'todos': Todo.objects.all(),
#         'form': CreateTodoForm(),
#     }
#
#     return render(request, 'index.html', context)
#
#
# def create_todo(request):
#     form = CreateTodoForm(request.POST)
#
#     if form.is_valid():
#         # cleaned_data is available ONLY
#         # after the `i0s_valid()` call
#         text = form.cleaned_data['text']
#         description = form.cleaned_data['description']
#         todo = Todo(
#             text=text,
#             description=description,
#             # owner=owner,
#         )
#         todo.save()
#         return redirect('/')
#     else:
#         context = {
#             'todos': Todo.objects.all(),
#             'form': form,
#         }
#
#         return render(request, 'index.html', context)
#
#
# def change_todo_state(request, pk):
#     todo = Todo.objects.get(pk=pk)
#     todo.state = not todo.state
#     todo.save()
#     return redirect('/')
from todos_app.todos.models import Todo


def index(request):
    context = {
        'todos': Todo.objects.all(),
    }
    return render(request, 'todo_app/index.html', context)


def create_todo(request):
    form = CreateTodoForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            todo = Todo(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                state=False,
            )
            todo.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'todo_app/create.html', context)


def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    form = UpdateTodoForm(request.POST, initial=todo)

    if request.method == 'POST':
        if form.is_valid():
            todo.title = form.cleaned_data['title']
            todo.description = form.cleaned_data['description']
            todo.state = form.cleaned_data['state']
            todo.save()
            return redirect('index')

    context = {
        'form': form,
    }

    return render(request, 'todo_app/create.html', context)
