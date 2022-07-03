from Client_ import Client

class GeneralClient(Client):
    def __init__(self, name, id, age, selected_game, vip_seats):
        super().__init__(name, id, age, selected_game)
        self.type_ticket = 1
        self.general_seats = vip_seats