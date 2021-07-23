from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name="index"),
    path('', views.IndexView.as_view(), name="index"),
    path('create/', views.PythonCreateView.as_view(), name="create"),
]
