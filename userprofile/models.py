from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username
