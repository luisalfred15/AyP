from funciones import * #24 de junio: Batalla de Carabobo; 5 de julio: Firma del Acta de la Independencia
import random

def main():

    clientes = []
    regalado = 0
    total_depositado = 0
    total_retirado = 0
    cont_oper = 0
    cont_clientes = 0
    
    print('Bienvenido a Saman Banks!')

    while True:
        opcion = comprobar_opcion('''Seleccione la opcion que desea realizar:
        1. Registrar un nuevo cliente
        2. Consulta saldo
        3. Deposito
        4. Retiro
        5. Salir del sistema
        -> ''', 5)

        if opcion == 1:

            nuevo_cliente = registrar_cliente()
            clientes.append(nuevo_cliente)
        
        elif opcion == 2:
            cedula = comprobar_num('Ingrese la cedula del cliente que desea buscar: ')
            cliente = buscar_cliente(cedula, clientes)
            if cliente == None:
                print('No se encontro el cliente deseado')  
            else:
                cliente.imprimir_cliente()
                cont_clientes += 1

        elif opcion == 3:

            operacion = 'Deposito'
            cedula = comprobar_num('Ingrese la cedula del cliente que desea buscar: ')

            cliente = buscar_cliente(cedula, clientes)
            if cliente == None:
                print('No se encontro el cliente deseado')  
            else:
                
                monto = comprobar_num('Ingrese la cantidad de dinero que desea depositar: ')
                if cliente.cuenta.tipo_cuenta == 'Ahorro':
                    regalado += monto * 0.1
                    total_depositado += monto + regalado
                    cliente.cuenta.saldo += monto + regalado
                    imprimir_factura(cliente, operacion, monto)
                    cont_clientes += 1


                else:
                    cliente.cuenta.saldo += monto
                    total_depositado += monto
                    imprimir_factura(cliente, operacion, monto)
                    cont_clientes += 1


        
        elif opcion == 4:
            operacion = 'Retiro'
            cedula = comprobar_num('Ingrese la cedula del cliente que desea buscar: ')
            
            cliente = buscar_cliente(cedula, clientes)
            if cliente == None:
                print('No se encontro el cliente deseado')  
            else:
                
                monto = comprobar_num('Ingrese la cantidad de dinero que desea retirar: ')
                if monto < cliente.cuenta.saldo:
                    total_retirado += monto
                    cliente.cuenta.saldo -= monto
                    imprimir_factura(cliente, operacion, monto)
                    cont_clientes += 1

                else:
                    print('No puede retirar mas dinero que el saldo con el que cuenta')
        
        else:
            imprimir_estadisticas(regalado, total_depositado, total_retirado, cont_oper, cont_clientes)
            break
                








main()