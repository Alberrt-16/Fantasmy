from team.models import TeamPlayer
from players.models import Player
from market.models import MarketListing

class MarketActions:

    @staticmethod
    def list_player(team, player, price):
        if not TeamPlayer.objects.filter(team=team, player=player).exists():
            raise Exception("No tienes este jugador")

        if MarketListing.objects.filter(player=player, is_active=True).exists():
            raise Exception("El jugador ya está en el mercado")

        MarketListing.objects.create(
            player=player,
            seller=team,
            price=price,
            listing_type='user'
        )

        return True


    @staticmethod
    def cancel_listing(team, listing):
        if listing.seller != team:
            raise Exception("No puedes cancelar esta venta")

        if not listing.is_active:
            raise Exception("El listing ya está inactivo")

        listing.is_active = False
        listing.save()

        return True


    @staticmethod
    def buy_from_market(team, listing):

        if not listing.is_active:
            raise Exception("Este jugador ya no está disponible")

        player = listing.player

        if team.budget < listing.price:
            raise Exception("No tienes suficiente dinero")

        if TeamPlayer.objects.filter(team=team, player=player).exists():
            raise Exception("Ya tienes este jugador")

        if listing.seller:
            seller_team = listing.seller

            relation = TeamPlayer.objects.filter(
                team=seller_team,
                player=player
            ).first()

            if relation:
                relation.delete()

            seller_team.budget += listing.price
            seller_team.save()

        TeamPlayer.objects.create(
            team=team,
            player=player
        )

        team.budget -= listing.price
        team.save()

        listing.is_active = False
        listing.save()

        return True