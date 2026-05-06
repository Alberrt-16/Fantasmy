import requests
from django.core.management.base import BaseCommand
from apps.players.models import Player


API_KEY = "1555ebd34df344deb346189ef5f44753"


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        Player.objects.all().delete()

        url = "https://api.football-data.org/v4/competitions/PD/teams"

        headers = {
            "X-Auth-Token": API_KEY
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        players_created = set()

        for team in data["teams"]:

            team_name = team["name"]

            team_id = team["id"]

            players_url = f"https://api.football-data.org/v4/teams/{team_id}"

            team_data = requests.get(players_url, headers=headers).json()

            squad = team_data.get("squad", [])

            for p in squad:

                name = p["name"]
                position_api = p["position"]

                if not name or name in players_created:
                    continue

                players_created.add(name)
                if position_api == "Goalkeeper":
                    position = "POR"
                elif position_api == "Defence":
                    position = "DEF"
                elif position_api == "Midfield":
                    position = "MED"
                else:
                    position = "DEL"

                Player.objects.create(
                    name=name,
                    position=position,
                    team=None,
                    price=10_000_000,
                    points=0,
                    is_active=True
                )

        self.stdout.write(self.style.SUCCESS("LaLiga players imported successfully"))