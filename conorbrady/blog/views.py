from django.views import generic

# Create your views here.

class BlogList(generic.ListView):
    # This works to pull only the lastest slug,
    # but only with postgres
    #
    # Workaround is to have management command mark older articles as inactive
    # Articles.objects.all().order_by('modified_date').distinct('slug')


    pass

class BlogDetail(generic.DetailView):
    pass
