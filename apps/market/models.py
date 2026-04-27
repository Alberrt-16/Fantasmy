from django.db import models
from apps.players.models import Player
from apps.team.models import Team


class Transfer(models.Model):

    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    from_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        related_name='sold_players'
    )

    to_team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        related_name='bought_players'
    )

    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)