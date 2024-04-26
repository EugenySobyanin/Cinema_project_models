from django import forms
from .models import WatchedFilms

class FilmForm(forms.ModelForm):
    
    class Meta:
        model = WatchedFilms
        fields = '__all__'