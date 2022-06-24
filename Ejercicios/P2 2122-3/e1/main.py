from funciones import *
from BebidaAlcoholica_ import BebidaAlcoholica
from BebidaNoAlcoholica_ import BebidaNoAlcoholica

def main():
    clientes = []
    bebidas_alco = []
    bebidas_no_alco = []
    mesas = {}
    print('Bienvenido a Saman Bar!')
    while True:
        opcion = comprobar_opcion('''Ingrese la opcion deseada:
        1. Añadir una bebida nueva
        2. Registrar un cliente
        3. Registrar una compra
        -> ''', 3)

        if opcion == '1':
            opcion_añadir = '1'
            while opcion_añadir == '1':
                tipo_beb = comprobar_opcion('''Seleccione el tipo de bebida:
                1. Alcoholica
                2. No alcoholica
                -> ''', 2)

                if tipo_beb == '1':

                    bebidas_alco = añadir_beb_alco(bebidas_alco)
                    print('Bebida alcoholica aniadida')
                
                else:

                    bebidas_no_alco = añadir_beb_no_alco(bebidas_no_alco)
                    print('Bebida no alcoholica aniadida')
                
                opcion_añadir = comprobar_opcion('''Desea añadir otra bebida?
                1. Si
                2. No
                -> ''', 2)
            
        elif opcion == '2':

            clientes = añadir_cliente(clientes)
            
        elif opcion == '3':

            for cliente in clientes:
                print(f'--- {clientes.index(cliente)} ---')
                cliente.imprimir_cliente()
            
            seleccion_cliente = comprobar_num('Seleccione el cliente al que le desea agregar un pedido: ')
            cliente_seleccionado = clientes[int(seleccion_cliente)]

            if cliente_seleccionado.edad >= 18:
                for bebida in bebidas_alco:
                    print(f'--- {bebidas_alco.index(bebida)} ---')
                    bebida.imprimir_beb_no_alc()
                
                seleccion_bebida = comprobar_num('Seleccione la bebida que desea agregar al pedido: ')
                bebida_seleccionada = bebidas_alco[int(seleccion_bebida)]
                cliente_seleccionado.pedido.append(bebida_seleccionada)
                print('Bebida aniadida')


main()