from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('admin_total', 'Admin Total'),
        ('admin_league', 'Admin Liga'),
        ('user', 'Usuario Comun'),
    )

    name = models.CharField(max_length=36, default='El Pepe')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
def __str__(self):
        return self.username
# Create your models here.
