class Event:
    def __init__(self, number, race_list):
        self.number = number
        self.race_list = list(race_list)
        self.race_number = len(self.race_list)
