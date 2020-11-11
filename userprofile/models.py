from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    email = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.user.username
