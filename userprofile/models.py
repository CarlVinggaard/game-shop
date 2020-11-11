from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    fullname = models.CharField(max_length=50, blank=True)
    email = models.CharField(max_length=40, unique=True, blank=True, null=True)
    phone = models.IntegerField(max_length=15, blank=True)
    address = models.CharField(max_length=40, blank=True)
    zipCode = models.IntegerField(max_length=6, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country = models.CharField(
        blank=True, choices=[("da", "Denmark"), ("gb", "Great Britain")]
    )

    def __str__(self):
        return self.user.username
