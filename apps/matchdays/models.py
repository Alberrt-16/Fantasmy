from django.db import models
from apps.players.models import Player
from apps.team.models import Team


class Matchday(models.Model):

    number = models.IntegerField(unique=True)
    start_date = models.DateField()
    end_date = models.DateField()

    is_active = models.BooleanField(default=False)
    is_finished = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Jornada {self.number}"


class PlayerMatchdayStats(models.Model):    

    RESULT_CHOICES = (
        ('win', 'Victoria'),
        ('draw', 'Empate'),
        ('loss', 'Derrota'),
    )

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    matchday = models.ForeignKey(Matchday, on_delete=models.CASCADE)

    goals = models.IntegerField(default=0)
    assists = models.IntegerField(default=0)
    key_passes = models.IntegerField(default=0)
    against_goals = models.IntegerField(default=0)
    lost_balls = models.IntegerField(default=0)
    clearences = models.IntegerField(default=0)
    final_result = models.CharField(max_length=4, choices=RESULT_CHOICES, default='draw')
    MVP = models.BooleanField(default=False)
    yellow_cards = models.IntegerField(default=0)
    red_cards = models.IntegerField(default=0)
    minutes_played = models.IntegerField(default=0)
    bonus_points = models.IntegerField(default=0)

    total_points = models.IntegerField(default=0)

    class Meta:
        unique_together = ('player', 'matchday')

    def __str__(self):
        return f"{self.player.name} - Jornada {self.matchday.number}"


class TeamMatchdayPoints(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    matchday = models.ForeignKey(Matchday, on_delete=models.CASCADE)

    points = models.IntegerField(default=0)

    captain_multiplier_applied = models.BooleanField(default=False)

    class Meta:
        unique_together = ('team', 'matchday')

    def __str__(self):
        return f"{self.team.name} - Jornada {self.matchday.number}"