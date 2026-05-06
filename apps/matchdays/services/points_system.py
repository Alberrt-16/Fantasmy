from matchdays.models import PlayerMatchdayStats
from team.models import Team, Lineup, LineupPlayer


class PointsSystem:

    @staticmethod
    def calculate_player_points(stats):

        points = 0

        points += stats.goals * 5
        points += stats.assists * 3
        points += stats.key_passes * 1

        points -= stats.yellow_cards * 1
        points -= stats.red_cards * 3

        points -= stats.lost_balls * 0.2
        points += stats.clearences * 0.5

        if stats.minutes_played >= 60:
            points += 2
        elif stats.minutes_played > 0:
            points += 1

        if stats.MVP:
            points += 3

        points += stats.bonus_points

        return round(points, 2)


    @staticmethod
    def update_all_player_points(matchday):

        stats_list = PlayerMatchdayStats.objects.filter(matchday=matchday)

        for stats in stats_list:
            stats.points = PointsSystem.calculate_player_points(stats)
            stats.save()


    @staticmethod
    def calculate_team_points(team, matchday):

        lineup = Lineup.objects.filter(team=team, matchday=matchday).first()

        if not lineup:
            return 0

        lineup_players = LineupPlayer.objects.filter(lineup=lineup)

        total_points = 0

        for lp in lineup_players:

            stats = PlayerMatchdayStats.objects.filter(
                player=lp.player,
                matchday=matchday
            ).first()

            if stats:
                player_points = stats.points

                if lineup.captain == lp.player:
                    player_points *= 2

                total_points += player_points

        return round(total_points, 2)


    @staticmethod
    def update_all_teams_points(matchday):

        teams = Team.objects.all()

        for team in teams:

            points = PointsSystem.calculate_team_points(team, matchday)

            team.points += points
            team.save()