from django.views import generic

class IndexView(generic.TemplateView):
    template_name = 'index.html'


class ResumeView(generic.TemplateView):
    template_name = 'index.html'