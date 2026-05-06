from django.db import models


class Team(models.Model):

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    league = models.ForeignKey('leagues.League', on_delete=models.CASCADE)

    name = models.CharField(max_length=36)
    budget = models.FloatField(default=100000000)
    points = models.IntegerField(default=0)

    players = models.ManyToManyField('players.Player', through='TeamPlayer', related_name='teams')

    def __str__(self):
        return self.name


class TeamPlayer(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE)

    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('team', 'player')


class Lineup(models.Model):

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    matchday = models.ForeignKey('matchdays.Matchday', on_delete=models.CASCADE)

    captain = models.ForeignKey(
        'players.Player',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='captain_lineups'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('team', 'matchday')


class LineupPlayer(models.Model):

    lineup = models.ForeignKey(Lineup, on_delete=models.CASCADE)
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE)

    is_starter = models.BooleanField(default=True)

    class Meta:
        unique_together = ('lineup', 'player')