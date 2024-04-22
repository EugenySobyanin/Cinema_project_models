from django.shortcuts import render
from .models import WatchedFilms

def film_list(request):
    films = WatchedFilms.objects.all()
    context = {'films': films}
    template = 'watched_films/watched_films.html'
    return render(request, template, context)
