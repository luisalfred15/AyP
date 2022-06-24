from os import stat


class Game:
    def __init__(self, teams, stadium, referee, status):
        self.teams = teams
        self.stadium = stadium
        self.referee = referee
        self.status = status