from funciones import *

def main():

    bebidas_alco = []
    bebidas_no_alco = []
    clientes = {}
    contador_clientes = 0
    contador_beb_alc = 0
    contador_beb_no_alc = 0

    print('Bienvenido a Saman Bar!')

    while True:
        opcion = comprobar_opcion('''Seleccione una de las opciones: 
        1. Registrar una nueva bebida
        2. Añadir un cliente
        3. Añadir la compra de un cliente
        4. Generar factura
        5. Generar estadisticas
        6. Salir del sistema
        -> ''', 6)

        if opcion == '1':

            opcion_tipo = comprobar_opcion('''Seleccione que tipo de bebida desea añadir:
            1. Alcoholica
            2. No alcoholica
            -> ''', 2)

            if opcion_tipo == '1':

                nueva_bebida_alco = generar_beb_alco()
                bebidas_alco.append(nueva_bebida_alco)
                contador_beb_alc += 1
            
            else:

                nueva_bebida_no_alco = generar_beb_no_alco()
                bebidas_no_alco.append(nueva_bebida_no_alco)
                contador_beb_no_alc += 1
            
        elif opcion == '2':

            contador_clientes += 1
            nuevo_cliente = generar_cliente()
            clientes[contador_clientes] = nuevo_cliente
            
        
        elif opcion == '3':

            if contador_clientes > 0:
                print('*** CLIENTES ***')
                for key, value in clientes.items():
                    print(f'ID: {key}')
                    value.imprimir_cliente()
                
                selecc_cliente = comprobar_opcion('Ingrese el ID del cliente al que le desea añadir un pedido: ', contador_clientes)
                selecc_cliente = int(selecc_cliente)
            
            else:
                print('No es posible seleccionar un cliente ya que no hay clientes registrados')

            if clientes[selecc_cliente].edad >= 18:
                
                flag_bebidas = False

                if len(bebidas_alco) > 0:
                    print('\n *** BEBIDAS ALCHOLICAS *** \n')
                    for bebida in bebidas_alco:
                        print(f'ID: {bebidas_alco.index(bebida) + 1}')
                        bebida.imprimir_beb_alco()
                    flag_bebidas = True
                else:
                    print('No hay bebidas alcoholicas que mostrar')

                if len(bebidas_no_alco) > 0:
                    print('*** BEBIDAS NO ALCHOLICAS *** \n')
                    for bebida in bebidas_no_alco:
                        print(f'ID: {bebidas_no_alco.index(bebida) + 1}')
                        bebida.imprimir_beb_no_alco()
                    flag_bebidas = True
                else:
                    print('No hay bebidas no alcoholicas que mostrar')

                if flag_bebidas:
                    selecc_tipo = comprobar_opcion('''Seleccione el tipo de bebida que va a añadir al pedido:
                    1. Alcoholica
                    2. No alcoholica
                    -> ''', 2)

                    if selecc_tipo == '1':

                        id_selecc = comprobar_opcion('Ingrese el ID de la bebida a añadir: ', len(bebidas_alco))
                        id_selecc = int(id_selecc) - 1
                        clientes[selecc_cliente].pedido.append(bebidas_alco[id_selecc])
                    
                    else:

                        id_selecc = comprobar_opcion('Ingrese el ID de la bebida a añadir: ', len(bebidas_no_alco))
                        id_selecc = int(id_selecc) - 1
                        clientes[selecc_cliente].pedido.append(bebidas_no_alco[id_selecc])
            
            else:

                if len(bebidas_no_alco) > 0:
                    print('\n *** BEBIDAS NO ALCHOLICAS *** \n')
                    for bebida in bebidas_no_alco:
                        print(f'ID: {bebidas_no_alco.index(bebida) + 1}')
                        bebida.imprimir_beb_no_alco()
                    flag_bebidas = True
                else:
                    print('No hay bebidas no alcoholicas que mostrar')
                
                if flag_bebidas:

                        id_selecc = comprobar_opcion('Ingrese el ID de la bebida a añadir: ', len(bebidas_alco))
                        id_selecc = int(id_selecc) - 1
                        clientes[selecc_cliente].pedido.append(bebidas_alco[id_selecc])
        
        elif opcion == '4':

            if contador_clientes > 0:
                print('*** CLIENTES ***')
                for key, value in clientes.items():
                    print(f'''ID: {key}
                    Nombre: {value.nombre}''')
                    
                
                selecc_factura = comprobar_opcion('Ingrese el ID del cliente al que le desea imprimir la factura: ', contador_clientes)
                selecc_factura = int(selecc_factura)

                imprimir_factura(clientes[selecc_factura])
            
            else:
                print('No se puede imprimir la factura porque no hay clientes registrados')
        
        elif opcion == '5':

            

                


        else:
            break


                





main()