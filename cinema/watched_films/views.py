from django.shortcuts import render
from .models import WatchedFilms
from .forms import FilmForm

def film_list(request):
    films = WatchedFilms.objects.all()
    context = {'films': films}
    template = 'watched_films/watched_films.html'
    return render(request, template, context)


def add_watched_film(request):
    template = 'watched_films/add_watched.html'
    form = FilmForm()
    context = {'form':form}
    return render(request, template, context)