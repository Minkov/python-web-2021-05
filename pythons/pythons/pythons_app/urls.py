from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('create/', views.create, name="create"),
    path('sign-in/', views.sign_in, name='sign in'),
    path('sign-out/', views.sign_out, name='sign out'),
]
