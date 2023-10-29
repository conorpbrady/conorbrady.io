from django.views import generic
from .models import Article, Label
# Create your views here.

class BlogList(generic.ListView):
    # This works to pull only the lastest slug,
    # but only with postgres
    #
    # Workaround is to have management command mark older articles as inactive
    # Articles.objects.all().order_by('modified_date').distinct('slug')

    template_name = 'blog/index.html'
    context_object_name = 'articles'
    ordering = ['-pub_date']

    def get_queryset(self):
        return Article.objects.filter(active = True)

class BlogDetail(generic.DetailView):
    template_name = 'blog/article.html'
    # result = Article.objects.get(id = id)

    def get_queryset(self):
        return Article.objects.filter(active = True)
