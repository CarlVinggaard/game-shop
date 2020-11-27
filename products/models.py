from django.db import models
from django.contrib.postgres.fields import ArrayField


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    min_players = models.PositiveIntegerField()
    max_players = models.PositiveIntegerField()
    min_age = models.PositiveIntegerField()
    img_url = models.URLField(max_length=512)
    min_playing_time = models.PositiveIntegerField()
    max_playing_time = models.PositiveIntegerField()
    complexity_rating = models.DecimalField(max_digits=4, decimal_places=2)
    rating = models.DecimalField(max_digits=4, decimal_places=2)
    description = models.TextField()
    categories = ArrayField(models.CharField(max_length=64))
    featured = models.BooleanField(default=False)
    deal = models.IntegerField(
        choices=[
            (val, val) for val in range(0, 100, 5)
        ],  # A deal is a percentage price reductions (between 0 and 100 % and a multiple of 5)
        null=True,
    )
    release_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name
