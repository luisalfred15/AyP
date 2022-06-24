from Module_1 import *
from functions import *

def main():
    db = get_json()
    
    print('Bienvenido al sistema de la liga El Saman!')

    while True:
        option = comprobar_opcion('''Ingrese la operacion que desea realizar:
        1. Mostrar equipos
        Otro. Salir del sistema
        -> ''', 2)

        if option == '1':
            players = create_objects_players(db)
            stadiums = create_objects_stadiums(db)
            teams = create_objects_teams(db, players, stadiums)

            show_teams(teams)
            
        
        else:
            break
            








main()