from django.db import models

class Player(models.Model):

    POSITION_CHOICES = (
        ('POR', 'Portero'),
        ('DEF', 'Defensa'),
        ('MED', 'Centrocampista'),
        ('DEL', 'Delantero'),
    )

    STATUS_CHOICES = (
        ('LES', 'Lesionado'),
        ('DIS', 'Disponible'),
        ('DUD', 'Dudoso'),
        ('NOD', 'No disponible'),
    )

    name = models.CharField(max_length=100)
    position = models.CharField(max_length=3, choices=POSITION_CHOICES)
    status = models.CharField(max_length=3, choices=STATUS_CHOICES, default='DIS')

    team = models.ForeignKey(
    'team.Team',         
    on_delete=models.SET_NULL,
    null=True,
    blank=True,
    related_name='FutPlayers',
)


    price = models.FloatField(default=10000000)
    points = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name