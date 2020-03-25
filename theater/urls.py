from django.urls import path

from .views import index, affiche, film_detail, news, news_detail

app_name = 'theater'

urlpatterns = [
    path('', index, name='index'),
    path('affiche/', affiche, name='affiche'),
    path('film/<slug:slug>', film_detail, name='film_detail'),
    path('news/', news, name='news'),
    path('news/<slug:slug>', news_detail, name='news_detail')
]