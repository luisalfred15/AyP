from functions import *
import random
from Game_ import *

def get_referees(db):
    referees = []
    for referee in db['referees']:
        referees.append(referee)
    return referees

def create_game(teams, stadiums, referees):
    games = []
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

def generate_result(team1, team2):
    points1 = 0
    points2 = 0
    ref_num = str(random.randint(0, 10000))
    if ref_num[-1] == '1':
        points1 += 1
    elif ref_num[-1] == '2':
        points2 += 1
    result = f'{team1.name}: {points1} | {team2.name}: {points2}'
    return result

def change_status_game(games):
    for game in games:
        print(f'''ID: {games.index(game) + 1} {game.team1} vs. {game.team2}
                        Estadio: {game.stadium}
                        Arbitro: {game.referee}''')
    game_selected = comprobar_opcion('Seleccione el partido al que desea habilitar la venta de entradas: ', len(games))
    games[game_selected - 1].status = True
    game_status = games[game_selected - 1].status
    return game_status

