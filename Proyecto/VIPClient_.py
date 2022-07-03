from Client_ import *

class VIPClient(Client):
    def __init__(self, name, id, age, selected_game, vip_seats):
        super().__init__(name, id, age, selected_game)
        self.type_ticket = 2
        self.vip_seats = vip_seats
        self.foods = []