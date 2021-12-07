from django.core.management.base import BaseCommand
from scores.models import Team, Tournament, Fixture

TEAMS = [
    'Chelsea', 'Man City', 'Liverpool', 'West Ham', 'Arsenal', 'Wolves', 'Tottenham',
    'Man Utd', 'Brighton', 'Crystal Palace', 'Everton', 'Leicester', 'Southampton',
    'Brentford', 'Aston Villa', 'Watford', 'Leeds', 'Burnley', 'Norwich', 'Newcastle'
]

class Command(BaseCommand):
    help = 'Load EPL teams and fixtures'

    def handle(self, *args, **kwargs):
        # add the tournament
        tournament = Tournament.objects.get_or_create(name="Premier League")[0]

        # add the teams
        if Team.objects.count() == 0:
            team_objs = [Team(name=team_name) for team_name in TEAMS]
            teams = Team.objects.bulk_create(team_objs)
            teams = Team.objects.all()
        else:
            teams = Team.objects.all()

        # Next step: create a set of fixtures from the teams list

        fixtures = []
        for i in range(0, len(teams), 2):
            fixtures.append(
                Fixture(home_team=teams[i], away_team=teams[i+1], tournament=tournament)
            )

        # bulk create the fixtures
        if Fixture.objects.count() == 0:
            fixtures = Fixture.objects.bulk_create(fixtures)        