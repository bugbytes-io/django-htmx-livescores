from django.db import models

# Create your models here.
class Tournament(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Fixture(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='fixtures')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_games')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_games')
    home_goals = models.PositiveSmallIntegerField(default=0)
    away_goals = models.PositiveSmallIntegerField(default=0)
    game_finished = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.home_team} vs {self.away_team}"