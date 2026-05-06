from django.db import models


class MarketListing(models.Model):

    LISTING_TYPE = (
        ('system', 'Sistema'),
        ('user', 'Usuario'),
    )

    player = models.ForeignKey(
        'players.Player',
        on_delete=models.CASCADE,
        related_name='market_listings'
    )

    seller = models.ForeignKey(
        'team.Team',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='selling_listings'
    )

    price = models.FloatField()

    listing_type = models.CharField(
        max_length=10,
        choices=LISTING_TYPE
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.player.name} - {self.price} ({self.listing_type})"