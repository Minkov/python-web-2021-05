from django.shortcuts import render, redirect

from todos_app.todos.models import Todo
from todos_app.todos.models.todo import Person


def index(request):
    context = {
        'todos': Todo.objects.all(),
    }

    return render(request, 'index.html', context)


def create_todo(request):
    text = request.POST['text']
    description = request.POST['description']
    owner_name = request.POST['owner']
    owner = Person.objects \
        .filter(name=owner_name) \
        .first()

    if not owner:
        owner = Person(name=owner_name)
        owner.save()

    todo = Todo(
        text=text,
        description=description,
        owner=owner,
    )
    todo.save()

    # print(Person.objects.raw("select * from todos_person"))

    return redirect('/')


def change_todo_state(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.state = not todo.state
    todo.save()
    return redirect('/')
