from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todos_app.todos.urls')),
    path('forms/', include('todos_app.forms_workshop.urls')),
]
