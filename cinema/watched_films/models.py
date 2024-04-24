from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from datetime import datetime

cur_year = datetime.now().year

# модель с оригинальными названиями фильмов  
class OriginalTitle(models.Model):
    title = models.CharField(max_length=128, unique=True)
    add_time = models.DateTimeField(auto_created=True, null=True)
    

    class Meta:
        ordering = ('add_time',)
        
            
# модель c жанрами фильмов
class Genre(models.Model):
    genre_title = models.CharField(max_length=128, unique=True)
    add_time = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('add_time',)
        
    
    def __str__(self):
        return self.genre_title   


# модель с типами (например: фильм, мультфильм, сериал)
class ProductType(models.Model):
    type_title = models.CharField(max_length=128)
    
    
    class Meta:
        ordering = ('id',)
        
        
    def __str__(self):
        return self.type_title
    

# моделль с просмотренными фильмами
class WatchedFilms(models.Model):
    title = models.CharField("Название", max_length=128, unique=True)
    year = models.PositiveSmallIntegerField("Год", null=True, validators=
                                            [MinValueValidator(1900), 
                                             MaxValueValidator(cur_year + 20)
                                             ]
                                            )
    original_title = models.OneToOneField(
        OriginalTitle,
        blank=True, 
        null=True, 
        on_delete=models.SET_NULL, 
        verbose_name="Оригинальное название") # связь один к одному
    kp_mark = models.FloatField("Рейтинг", blank=True)
    product_type = models.ForeignKey(
        ProductType,
        blank=True,
        on_delete=models.SET_NULL,
        null=True
    )
    genres = models.ManyToManyField(Genre, blank=False, verbose_name="Жанр")
    country = models.CharField("Страна", max_length=128)
    add_time = models.DateTimeField(auto_now_add=True, null=True)

    
    
    class Meta:
        ordering = ('add_time',)
        
        
    def __str__(self):
        return self.title
    

    
