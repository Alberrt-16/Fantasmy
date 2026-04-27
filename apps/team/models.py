from django.db import models
from apps.users.models import User
from apps.leagues.models import League
from apps.players.models import Player


class Team(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    name = models.CharField(max_length=36)
    budget = models.FloatField(default=100000000)
    points = models.IntegerField(default=0)

    players = models.ManyToManyField(Player, through='TeamPlayer', related_name='teams')

    def __str__(self):
        return self.name


class TeamPlayer(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    joined_at = models.DateTimeField(auto_now_add=True)