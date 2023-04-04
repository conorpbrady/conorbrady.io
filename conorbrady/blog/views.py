from django.views import generic

# Create your views here.

class BlogList(generic.ListView):
    pass

class BlogDetail(generic.DetailView):
    pass
