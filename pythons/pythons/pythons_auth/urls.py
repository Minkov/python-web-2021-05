from django.urls import path

from pythons.pythons_auth import views

urlpatterns = (
    path('sign-up/', views.sign_up, name='sign up'),
    path('sign-in/', views.sign_in, name='sign in'),
    path('sign-out/', views.sign_out, name='sign out'),
)
