from Module_1 import *
from Module_2 import *
from Module_3 import *
from Module_4 import *
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
    products = create_objects_products(db)
    load_data('Products_DB.txt', products)
    
    print('Bienvenido al sistema de la liga El Saman!')

    while True:
        option = comprobar_opcion('''Ingrese la operacion que desea realizar:
        1. Buscar equipos
        2. Crear partidos
        3. Abrir venta de entradas
        4. Vender entradas
        5. Cerrar venta de entradas y ver resultados de partidos
        6. Buscar comidas o bebidas
        7. Adquirir un producto del restaurante
        8. Reiniciar base de datos
        Otro. Salir del sistema
        -> ''', 9)

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
            clients = read_data('Clients.txt', [])
            invoices = read_data('Invoices.txt', [])
            
            games = read_data('Games.txt', [])
            everything_closed = verify_games_opened(games)
            if everything_closed == True:
                print('No se pueden vender entradas ya que no hay partidos disponibles')
            else:
                clients, invoices = register_client_and_invoice(games, clients, invoices)
            
            load_data('Invoices.txt', invoices)
            load_data('Clients.txt', clients)
        
        elif option == 5:
            
            games = read_data('Games.txt', [])
        
        elif option == 6:
            
            products = read_data('Products_DB.txt', [])
            show_products(products)

        elif option == 7:
            products = read_data('Products_DB.txt', [])
            clients = read_data('Clients.txt', [])
            invoices_rest = read_data('InvoicesRestaurant.txt', [])

            vip_client, invoices_rest = register_client_restaurant(clients, products, invoices_rest)
            if vip_client == -1:
                pass
            elif vip_client == -2:
                print('El cliente VIP no pudo ser encontrado')
            
            load_data('Clients.txt', vip_client)
            load_data('Products_DB.txt', products)
            load_data('InvoicesRestaurant.txt', invoices_rest)
        
        elif option == 8:
            restart_everything()
            print('Base de datos reiniciada con exito')

        else:
            break
            








main()