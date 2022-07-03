from Module_1 import *
from Module_2 import *
from functions import *

def main():
    db = get_json()

    players = create_objects_players(db)
    load_data('Players_DB.txt', players)
    stadiums = create_objects_stadiums(db)
    load_data('Stadiums_DB.txt', stadiums)
    teams = create_objects_teams(db, players, stadiums)
    load_data('Teams_DB.txt', teams)
    referees = get_referees(db)
    load_data('Referees_DB.txt', referees)
    
    print('Bienvenido al sistema de la liga El Saman!')

    while True:
        option = comprobar_opcion('''Ingrese la operacion que desea realizar:
        1. Mostrar equipos
        2. Crear partidos
        3. Abrir venta de entradas
        4. Vender entradas
        5. Ver resultados de partidos
        Otro. Salir del sistema
        -> ''', 6)

        if option == 1:

            teams = read_data('Teams_DB.txt', [])
            show_teams(teams)
            
        elif option == 2:
            teams = read_data('Teams_DB.txt', [])
            stadiums = read_data('Stadiums_DB.txt', [])
            referees = read_data('Referees_DB.txt', [])
            games = create_game(teams, stadiums, referees)
            load_data('Games.txt', games)

        elif option == 3:
            
            games = read_data('Games.txt', [])
            change_status_game(games)
            load_data('Games.txt', games)
        
        elif option == 4:

            games = read_data('Games.txt', [])
            register_client(games)
            

        else:
            break
            








main()