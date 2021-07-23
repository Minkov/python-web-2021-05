from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.views.generic.detail import SingleObjectMixin

from articles.web.models import Article, Source


class ArticleCreateView(views.CreateView):
    model = Article
    template_name = 'web/create-article.html'
    success_url = reverse_lazy('index')
    fields = '__all__'


class SourceCreateView(views.CreateView):
    model = Source
    template_name = 'web/create-source.html'
    # success_url = reverse_lazy('index')
    fields = '__all__'

    def get_success_url(self):
        return reverse('details source', kwargs={
            'pk': self.object.id,
        })


class ArticlesListView(views.ListView):
    model = Article
    template_name = 'web/list-articles.html'


class SourceDetailsView(SingleObjectMixin, views.ListView):
    model = Source
    template_name = 'web/details-source.html'
    object = None
    paginate_by = 3

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Source.objects.all())
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['source'] = self.object
        return context

    def get_queryset(self):
        return self.object.article_set.all()


class SourcesListView(views.ListView):
    model = Source
    template_name = 'web/list-sources.html'
