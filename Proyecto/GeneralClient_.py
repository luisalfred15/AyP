from Client_ import Client

class GeneralClient(Client):
    def __init__(self, name, id, age, selec_game, type_ticket, general_seat):
        super().__init__(name, id, age, selec_game, type_ticket)
        self.general_seat = general_seat