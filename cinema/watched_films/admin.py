from django.contrib import admin
from .models import WatchedFilms, OriginalTitle, Genre, ProductType


admin.site.register(WatchedFilms)
admin.site.register(OriginalTitle)
admin.site.register(Genre)
admin.site.register(ProductType)
# Register your models here.
