from team.models import Lineup, LineupPlayer


class LineupService:

    @staticmethod
    def create_lineup(team, matchday, players, captain):

        if len(players) != 11:
            raise Exception("Debes seleccionar 11 jugadores")

        if captain not in players:
            raise Exception("El capitán debe estar en la alineación")

        lineup = Lineup.objects.create(
            team=team,
            matchday=matchday,
            captain=captain
        )

        for player in players:
            LineupPlayer.objects.create(
                lineup=lineup,
                player=player
            )

        return lineup