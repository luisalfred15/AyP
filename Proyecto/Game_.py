from functions import *

class Game:
    def __init__(self, team1, team2, stadium, referee):
        self.team1 = team1
        self.team2 = team2
        self.stadium = stadium
        self.referee = referee
        self.status = False
        self.result = ''
        self.audience = []
    
    def print_game(self):
        self.print_team_names()
        self.print_stadium()
        self.print_referee()
    
    def print_final_game(self):
        self.print_team_names()
        self.print_stadium()
        self.print_referee()
        self.print_result()
    
    def print_team_names(self):
        print(f'''{self.team1.name} vs. {self.team2.name}''')
    
    def print_stadium(self):
        print(f'Estadio: {self.stadium.name}')
    
    def print_referee(self):
        print(f'Arbitro: {self.referee}')
    
    def print_result(self):
        print(self.result)
    
    def select_general_seats(self, seats_to_buy, dict_seats = {}, client_seats = []):
        if seats_to_buy > 0:
            self.stadium.print_general_seats()
            selected_seat = input('Ingrese el asiento que desea comprar: ')
            for i in range(len(self.stadium.general_seats)):
                for j in range(len(self.stadium.general_seats[i])):
                    if self.stadium.general_seats[i][j] == selected_seat:
                        if self.stadium.general_seats[i][j] != 'X':
                            print(f'Asiento {selected_seat} seleccionado')
                            self.stadium.general_seats[i][j] = 'X'
                            dict_seats[selected_seat] = [i, j]
                            client_seats.append(selected_seat)
                            self.stadium.print_general_seats()
                            updated_seats = self.stadium.general_seats
                            return self.select_general_seats(seats_to_buy - 1, client_seats)
                        else:
                            print('Por favor, seleccione un asiento que este disponible')
                            return self.select_general_seats(seats_to_buy, client_seats)
            print('El asiento que ha seleccionado no existe')
            return self.select_general_seats(seats_to_buy)
        else:
            proceed = comprobar_opcion('''Desea proceder a la compra de los tickets o desea cambiar algun puesto?
            1. Proceder a la compra
            2. Cambiar algun puesto
            -> ''', 2)
            if proceed == 1:
                self.stadium.general_seats = updated_seats
                return client_seats
            else:
                client_seats = self.deselect_general_seats(dict_seats)
                return client_seats
    
    def deselect_general_seats(self, dict_seats, client_seats):
        for seat in client_seats:
            print(f'{client_seats.index(seat)}. {seat}')
        seat = comprobar_opcion('Seleccione el asiento que desea eliminar: ', len(client_seats))
        delete_seat = dict_seats.get(seat)
        self.stadium.general_seats[delete_seat[0]][delete_seat[1]] = seat
        dict_seats.pop(delete_seat)
        return client_seats
        
    def select_vip_seats(self, seats_to_buy, dict_seats = {}, client_seats = []):
        if seats_to_buy > 0:
            self.stadium.print_vip_seats()
            selected_seat = input('Ingrese el asiento que desea comprar: ')
            for i in range(len(self.stadium.vip_seats)):
                for j in range(len(self.stadium.vip_seats[i])):
                    if self.stadium.vip_seats[i][j] == selected_seat:
                        if self.stadium.vip_seats[i][j] != 'X':
                            print(f'Asiento {selected_seat} seleccionado')
                            self.stadium.vip_seats[i][j] = 'X'
                            dict_seats[selected_seat] = [i, j]
                            client_seats.append(selected_seat)
                            self.stadium.print_vip_seats()
                            updated_seats = self.stadium.vip_seats
                            return self.select_vip_seats(seats_to_buy - 1, client_seats)
                        else:
                            print('Por favor, seleccione un asiento que este disponible')
                            return self.select_vip_seats(seats_to_buy, client_seats)
            print('El asiento que ha seleccionado no existe')
            return self.select_vip_seats(seats_to_buy)
        else:
            proceed = comprobar_opcion('''Desea proceder a la compra de los tickets o desea cambiar algun puesto?
            1. Proceder a la compra
            2. Cambiar algun puesto
            -> ''', 2)
            if proceed == 1:
                self.stadium.vip_seats = updated_seats
                return client_seats
            else:
                client_seats = self.deselect_vip_seats(dict_seats)
                return client_seats
    
    def deselect_vip_seats(self, dict_seats, client_seats):
        for seat in client_seats:
            print(f'{client_seats.index(seat)}. {seat}')
        seat = comprobar_opcion('Seleccione el asiento que desea eliminar: ', len(client_seats))
        delete_seat = dict_seats.get(seat)
        self.stadium.vip_seats[delete_seat[0]][delete_seat[1]] = seat
        dict_seats.pop(delete_seat)
        return client_seats