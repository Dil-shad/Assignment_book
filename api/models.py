from turtle import tilt, title
from django.db import models

# Create your models here.


class GenreModel(models.Model):
    title = models.CharField(max_length=225)

    def __str__(self):
        return self.title


class eBook(models.Model):
    title = models.CharField(max_length=225)
    author = models.CharField(max_length=225)
    review = models.IntegerField()
    favorite = models.BooleanField(default=False)
    genre = models.ForeignKey(GenreModel, on_delete=models.CASCADE, null=True ,blank=True,related_name='genre_title')
    

    def __str__(self):
        return self.title
    @property
    def genre_title(self):
        return self.genre.title
    