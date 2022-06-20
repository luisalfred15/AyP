from funciones import *
from JuntaDirectiva_ import *
from JuntaDirectivaEscuela_ import *
from JuntaDirectivaGeneral_ import *
from Plancha_ import *

planchas = generar_bd_planchas()
jds = generar_bd_jds()

def main():
    print('Bienvenido al sistema electoral del FCE!')
    lista_jdg = []
    lista_jde = []
    lista_planchas = []
    while True:
        opcion = comprobar_opcion('''Seleccione la opcion deseada:
        1. Ver informacion de las planchas con sus Juntas Directivas
        2. Generar resultados
        3. Salir del sistema
        -> ''', 3)

        for element in planchas:
            nueva_plancha = Plancha(element.get('nombre'), element.get('numero'))
            lista_planchas.append(nueva_plancha)
        
        for element_2 in jds:
            if element_2.get('tipo') == 'G':
                nueva_jdg = JuntaDirectivaGeneral(element_2.get('presidente'), element_2.get('coordinador general'), element_2.get('tesorero'), element_2.get('plancha'), element_2.get('sg'), element_2.get('sai'))
                lista_jdg.append(nueva_jdg)
        
        for element_3 in jds:
            if element_3.get('tipo') == 'E':
                nueva_jde = JuntaDirectivaEscuela(element_3.get('presidente'), element_3.get('coordinador general'), element_3.get('tesorero'), element_3.get('plancha'), element_3.get('escuela'))
                lista_jde.append(nueva_jde)
        
        if opcion == '1':
            print('''*** PLANCHAS ***''')
            for element_4 in lista_planchas:
                print('======================')
                element_4.imprimir_plancha()
                print('======================')
                for element_5 in lista_jde:
                    if element_4.numero == element_5.plancha:
                        print('======================')
                        element_5.imprimir_jde()
                        print('======================')
                for element_6 in lista_jdg:
                    if element_4.numero == element_6.plancha:
                        print('======================')
                        element_6.imprimir_jdg()
                        print('======================')
        
        elif opcion == '2':

            carnet = comprobar_num('Ingrese su numero de carnet: ')         # 20211110067
            votos_v, votos_j, ganador = victoria_plancha(carnet)
            resultados = imprimir_victoria(votos_v, votos_j, ganador)
            guardar_resultados(resultados)
        
        elif opcion == '3':
            break

main()