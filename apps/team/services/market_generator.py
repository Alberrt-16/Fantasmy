import random
from players.models import Player
from team.models import TeamPlayer
from market.models import MarketListing


def generate_market():

    owned_players = TeamPlayer.objects.values_list('player_id', flat=True)
    free_players = Player.objects.exclude(id__in=owned_players)
    random_players = random.sample(list(free_players), min(10, free_players.count()))

    MarketListing.objects.filter(listing_type='system').delete()
    for player in random_players:
        MarketListing.objects.create(
            player=player,
            price=player.price,
            listing_type='system'
        )