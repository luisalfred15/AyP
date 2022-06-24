from functions import *
from Team_ import Team
from Player_ import Player
from Stadium_ import Stadium

# Crea los objetos de cada jugador y los añade a una lista de todos los jugadores de cada equipo

def create_objects_players(db):
    players = []
    for team in db['teams']:
        for key, value in team.items():
            if key == 'lineup':
                for player in value:
                    new_player = Player(player.get('name'), team.get('name'), player.get('number'), player.get('position'))
                    players.append(new_player)
    return players

# Crea los objetos de cada estadio y los añade a una lista

def create_objects_stadiums(db):
    stadiums = []
    for team in db['teams']:
        for key, value in team.items():
            if key == 'stadium':
                new_stadium = Stadium(value.get('name'), value['map']['general'], value['map']['vip'])
                stadiums.append(new_stadium)
    return stadiums

# Crea los objetos de cada equipo

def create_objects_teams(db, players, stadiums):
    teams = []
    for team in db['teams']:
        players_selected = []
        for player in players:                          # En este ciclo, se crea la lista de jugadores que se asociara con el objeto del equipo, ya que
            if team.get('name') == player.team:         # la otra lista contiene a todos los jugadores de la base de datos
                players_selected.append(player)
        for stadium in stadiums:                        # En este ciclo, se asigna el estadio del equipo
            if team['stadium']['name'] == stadium.name:
                stadium_selected = stadium
        new_team = Team(team.get('name'), players_selected, stadium_selected)
        teams.append(new_team)
    return teams

def show_teams(list_teams):
    option_teams = comprobar_opcion('''Seleccione como desea buscar a los equipos:
            1. Por nombre de equipo
            2. Por nombre de jugador
            3. Por nombre de estadio
            -> ''', 3)
    search(list_teams, option_teams)
    
def search(list_teams, option_teams):
    if option_teams == '1':
        print_by_team(list_teams)
    elif option_teams == '2':
        print_by_player(list_teams)
    else:
        print_by_stadium(list_teams)

def print_by_team(list_teams):
    team_found = False
    name = comprobar_str('Ingrese el equipo que desea buscar: ')
    while True:    
        for team in list_teams:
            if team.name == name:
                team_found = True
                team_to_print = team
        if team_found:
            print_team(team_to_print)
            break
        else:
            name = comprobar_str('Error, no se encontro el equipo. Ingrese el equipo que desea buscar: ')

def print_by_player(list_teams):
    player_found = False
    name = comprobar_str('Ingrese el nombre del jugador que desea buscar: ')
    while True:
        for team in list_teams:
            for player in team.lineup:
                if player.name == name:
                    player_found = True
                    team_to_print = team
        if player_found:
            print_team(team_to_print)
            break
        else:
            name = comprobar_str('Error, no se encontro el jugador. Ingrese el jugador que desea buscar: ')

def print_by_stadium(list_teams):
    stadium_found = False
    name = comprobar_str('Ingrese el estadio que desea buscar: ')
    while True:
        for team in list_teams:
            if team.stadium.name == name:
                stadium_found = True
                team_to_print = team
        if stadium_found:
            print_team(team_to_print)
            break
        else:
            name = comprobar_str('Error, no se encontro el estadio. Ingrese el estadio que desea buscar: ')

def print_team(team):
    print(f'''*** {team.name} ***''')
    print(f'Estadio {team.stadium.name}')
    print('*** POSICIONES ***')
    for player in team.lineup:
        print(f'''Nombre: {player.name}
        Posicion: {player.position}
        Numero: {player.number}''')