from Invoice_ import Invoice
from Module_4 import calculate_total
from functions import *
import random
from Game_ import *
from GeneralClient_ import *
from VIPClient_ import *
from Invoice_ import Invoice

####### Crear partidos y abrir la venta #######

def get_referees(db):
    referees = []
    for referee in db['referees']:
        referees.append(referee)
    return referees

def create_game(teams, stadiums, referees, games = []):
    team1, team2 = select_teams(teams)
    stadium = select_stadium(stadiums)
    referee = select_referee(referees)
    new_game = Game(team1, team2, stadium, referee)
    games.append(new_game)
    return games

def select_teams(teams):
    print('*** EQUIPOS ***')
    for team in teams:
        print(f'{teams.index(team) + 1}. {team.name}')
    selection_team1 = comprobar_opcion('Seleccione el primer equipo para el partido: ', len(teams))
    team1 = teams[selection_team1 - 1]
    selection_team2 = comprobar_opcion('Seleccione el segundo equipo para el partido: ', len(teams))
    while selection_team1 == selection_team2:
        selection_team2 = comprobar_opcion('Erros, no se puede seleccionar el mismo equipo. Por favor, seleccione un equipo: ', len(teams))
    team2 = teams[selection_team2 - 1]
    return team1, team2

def select_stadium(stadiums):
    print('*** ESTADIOS ***')
    for stadium in stadiums:
        print(f'{stadiums.index(stadium) + 1}. {stadium.name}')
    selection_stadium = comprobar_opcion('Seleccione el estadio donde desea que se de el juego: ', len(stadiums))
    stadium_selected = stadiums[selection_stadium - 1]
    return stadium_selected

def select_referee(referees):
    selection_referee = random.randint(0, len(referees) - 1)
    referee_selected = referees[selection_referee]
    print(f'El arbitro del partido sera {referee_selected}')
    return referee_selected

####### Cambiar el estatus del partido ########
                        
def change_status_game(games):
    counter = 0
    for game in games:
        if game.status == False:    
            print(f'ID: {games.index(game) + 1}')
            game.print_game()
        else:
            counter += 1
    if counter != len(games):
        game_selected = comprobar_opcion('Seleccione el partido al que desea habilitar la venta de entradas: ', len(games))
        games[game_selected - 1].status = True
    else:
        print('No se puede cambiar el estatus de algun juego ya que no hay ninguno creado o todos estan cerrados')

def verify_games_opened(games):
    games_not_opened = 0
    everything_closed = False
    for game in games:
        if game.status == False:
            games_not_opened += 1
    if games_not_opened == len(games):
        everything_closed = True
    return everything_closed

def close_game(games):
    for game in games:
        if game.status == True and game.results == '':    
            game.print_game()
    id_game_selected = comprobar_opcion('Seleccione el partido al que desea cerrar la venta de entradas: ', len(games))
    game_selected = games[id_game_selected - 1]
    game_selected.status = False

####### Crear el resulado del partido ########

def generate_result(team1, team2, games):
    points1 = 0
    points2 = 0
    counter = 0
    for game in games:
        if game.status == True and game.results == '':    
            game.print_game()
    id_game_selected = comprobar_opcion('Seleccione el partido al que desea cerrar la venta de entradas: ', len(games))
    game_selected = games[id_game_selected - 1]
    while counter < 100:
        ref_num = str(random.randint(0, 10000))
        if ref_num[-1] == '1':
            points1 += 1
        elif ref_num[-1] == '2':
            points2 += 1
        counter += 1
    result = f'{team1.name}: {points1} | {team2.name}: {points2}'
    game_selected.result = result
    
def register_client_and_invoice(games, clients, invoices):
    name = comprobar_str('Introduzca el nombre del cliente: ')
    id = comprobar_num('Introduzca la cedula del cliente: ')
    age = comprobar_num('Introduzca la edad del cliente: ')
    for game in games:
        print(f'ID: {games.index(game) + 1}')
        game.print_game()
    id_selected_game = comprobar_opcion('Introduzca el ID del juego que desea ver: ', len(games))
    selected_game = games[id_selected_game]
    selection_ticket = comprobar_opcion('''Seleccione que tipo de entrada desea comprar:
    1. General
    2. VIP
    -> ''', 2)
    if selection_ticket == 1:
        selection_ticket = 'General'
        selected_seats = selected_game.select_general_seats()
        new_invoice = generate_invoice(selected_seats, id, selection_ticket)
        new_client = GeneralClient(name, id, age, selected_game, selected_seats, new_invoice)
        clients.append(new_client)
        invoices.append(new_invoice)
        return clients, invoices
    else:
        selection_ticket = 'VIP'
        selected_seats = selected_game.select_vip_seats()
        new_invoice = generate_invoice(selected_seats, id, selection_ticket)
        new_client = VIPClient(name, id, age, selected_game, selected_seats, new_invoice)
        clients.append(new_client)
        invoices.append(new_invoice)
        return clients, invoices

def generate_invoice(selected_seats, id, selection_ticket):
    cost = calculate_cost(selected_seats, selection_ticket)
    discount = calculate_discount(id)
    tax = calculate_tax(cost, discount)
    total = calculate_total(cost, tax)
    new_invoice = Invoice(selected_seats, selection_ticket, cost, discount, tax, total)
    return new_invoice

def calculate_cost(seats, selection_ticket):
    cost = 0
    if selection_ticket == 'General':
        cost = 15 * len(seats)
    else:
        cost = 45 * len(seats)
    return cost

def calculate_discount(id):
    discount = 0
    vampire_id = False
    if vampire_id:
        discount = 0.5
    return discount

def calculate_tax(cost, discount):
    cost_with_discount = cost - discount
    return cost_with_discount * 0.16

def calculate_total(cost_with_discount, tax):
    return cost_with_discount + tax
