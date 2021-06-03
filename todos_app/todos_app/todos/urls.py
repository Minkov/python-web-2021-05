from django.urls import path

from todos_app.todos.views import index, create_todo, change_todo_state

urlpatterns = [
    path('', index),
    path('todos-add/', create_todo),
    path('todo-change-state/<int:pk>', change_todo_state),
]
