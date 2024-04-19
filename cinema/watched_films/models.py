from django.db import models


# модель с оригинальными названиями фильмов  
class OriginalTitle(models.Model):
    title = models.CharField(max_length=128, unique=True)
    
    
# модель c жанрами фильмов
class Genre(models.Model):
    genre_title = models.CharField(max_length=128, unique=True)
    
    
# модель с типами (например: фильм, мультфильм, сериал)
class ProductType(models.Model):
    type_title = models.CharField(max_length=128)
    

# моделль с просмотренными фильмами
class WatchedFilms(models.Model):
    title = models.CharField(max_length=128, unique=True)
    original_title = models.OneToOneField(
        OriginalTitle,
        blank=True, 
        null=True, 
        on_delete=models.SET_NULL) # связь один к одному
    kp_mark = models.FloatField(blank=True)
    product_type = models.ForeignKey(
        ProductType,
        blank=True,
        on_delete=models.SET_NULL,
        null=True
    )
    genres = models.ManyToManyField(Genre, blank=False)
    country = models.CharField(max_length=128)
    

    
