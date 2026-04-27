from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    ROLE_CHOICES = (
        ('admin_total', 'Admin Total'),
        ('admin_league', 'Admin Liga'),
        ('user', 'Usuario Comun'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='user')
def __str__(self):
        return self.username
# Create your models here.
