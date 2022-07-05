from Client_ import *

class VIPClient(Client):
    def __init__(self, name, id, age, selected_game, seats, invoice):
        super().__init__(name, id, age, selected_game, seats)
        self.type_ticket = 'VIP'
        self.seats = seats
        self.invoice = invoice
        self.foods = []