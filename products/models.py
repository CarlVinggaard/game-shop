from django.db import models
from django.contrib.postgres.fields import ArrayField


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    min_players = models.IntegerField()
    max_players = models.IntegerField()
    min_age = models.IntegerField()
    img_url = models.URLField(max_length=512)
    min_playing_time = models.IntegerField()
    max_playing_time = models.IntegerField()
    complexity_rating = models.DecimalField(max_digits=4, decimal_places=2)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    categories = ArrayField(models.CharField(max_length=64))

    def __str__(self):
        return self.name
