from django.urls import path
from . import views

app_name = "watched_films"

urlpatterns = [
    path('', views.film_list, name="film_list")
]
