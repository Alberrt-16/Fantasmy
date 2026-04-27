from django.db import models
from apps.users.models import User


class League(models.Model):

    name = models.CharField(max_length=32)
    description = models.CharField(max_length=150, default='')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_leagues')
    users = models.ManyToManyField(User, related_name='leagues')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name