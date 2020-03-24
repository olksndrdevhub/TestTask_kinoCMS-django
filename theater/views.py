from django.shortcuts import render
from django.utils.timezone import now, pytz, timedelta
from django.conf import settings

from .models import Film, FilmGallery, News, FilmShowSession

def index(request):
    user_timezone = pytz.timezone(settings.TIME_ZONE)
    context = {
        'films_today': Film.objects.filter(show_today=True),
        'films_soon': Film.objects.filter(show_soon=True),
        'date': now().astimezone(user_timezone)
    }
    return render(request, 'theater/index.html', context)

def affiche(request):
    context = {
        'films': Film.objects.filter(can_sell_ticket=True),
        'films_soon': Film.objects.filter(show_soon=True, can_sell_ticket=False),
    }
    return render(request, 'theater/affiche.html', context)

def film_detail(request, slug):
    film = Film.objects.get(slug=slug)  
    curentdatetime = now().date()
    sessions = FilmShowSession.objects.filter(film__slug=slug)
    
    print(dir(sessions.first().session))

    context = {
        'sessions': sessions,
        'film': Film.objects.get(slug=slug),
        'gallery': FilmGallery.objects.filter(film__slug=slug),
        'curentdatetime': curentdatetime,
    }
    return render(request, 'theater/film_detail.html', context)



