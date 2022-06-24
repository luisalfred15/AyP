from Client_ import *

class VIPClient(Client):
    def __init__(self, name, id, age, selec_game, type_ticket, vip_seat):
        super().__init__(name, id, age, selec_game, type_ticket)
        self.vip_seat = vip_seat
        self.foods = []