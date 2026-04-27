from django.db import models
from apps.leagues.models import League
from apps.team.models import Team


class Ranking(models.Model):

    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    points = models.IntegerField(default=0)
    position = models.IntegerField(default=0)

    updated_at = models.DateTimeField(auto_now=True)