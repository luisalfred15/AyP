class Game:
    def __init__(self, team1, team2, stadium, referee):
        self.team1 = team1
        self.team2 = team2
        self.stadium = stadium
        self.referee = referee
        self.status = False
        self.result = ''
        self.audience = []