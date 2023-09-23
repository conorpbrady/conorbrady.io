from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
        path('', views.BlogList.as_view(), name='index'),
        path('<slug:slug>', views.BlogDetail.as_view()),
        ]
