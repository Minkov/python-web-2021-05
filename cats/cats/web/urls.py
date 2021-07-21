from django.urls import path

from cats.web.views import show_cats, index, IndexView, ShowCatsListView, CatCreateView

urlpatterns = (
    path('', index, name='index'),
    path('cbv/', IndexView.as_view(), name='cbv index'),
    path('cbv/cats', ShowCatsListView.as_view(), name='cbv show cats'),
    path('cats/', show_cats, name='show cats'),
    path('create/', CatCreateView.as_view(), name='create cat'),
)
