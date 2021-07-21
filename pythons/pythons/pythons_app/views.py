from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Python


# def index(request):
#     pythons = Python.objects.all()
#     return render(request, 'index.html', {'pythons': pythons})
from ..core.mixins import AnyGroupRequiredMixin


class IndexView(ListView):
    template_name = 'index.html'
    model = Python
    context_object_name = 'pythons'
    paginate_by = 5


# @login_required(login_url=reverse_lazy('sign in'))
# @any_group_required(groups=['User'])
# def create(request):
#     if request.method == 'GET':
#         form = PythonCreateForm()
#         return render(request, 'create.html', {'form': form})
#     else:
#         form = PythonCreateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#
#         return render(request, 'create.html', {'form': form})


class PythonCreateView(AnyGroupRequiredMixin, CreateView):
    template_name = 'create.html'
    model = Python
    fields = '__all__'
    success_url = reverse_lazy('index')
