from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    karma = models.IntegerField(default=0)

    def __str__(self):
        return self.username
