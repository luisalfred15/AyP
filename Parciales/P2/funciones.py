from Cliente_ import Cliente                    
from CuentaAhorro_ import CuentaAhorro
from CuentaCorriente_ import CuentaCorriente
import random

def comprobar_str(msg):
    string = input(msg)
    if string.replace(' ', '').isalpha():
        return string
    else:    
        return comprobar_str('Error, ingrese palabras validas: ')

def comprobar_opcion(msg, cantidad_opciones):
    opcion = input(msg)
    if opcion.isnumeric() and int(opcion) in range(1, cantidad_opciones + 1):
        return int(opcion)
    else:
        return comprobar_opcion('Error, seleccione una opcion que este dentro del rango: ', cantidad_opciones)

def comprobar_num(msg):
    num = input(msg)
    if num.isnumeric() and 0 <= int(num):
        return int(num)
    else:
        return comprobar_num('Error, ingrese un numero valido: ')

def generar_num_cuenta():
        num_cuenta = random.randint(1, 1000000)
        return num_cuenta

def hallar_interes():
    interes = random.randint(1, 100)
    return interes

def registrar_cliente():
    nombre = comprobar_str('Ingrese el nombre del cliente: ')
    cedula = comprobar_num('Ingrese la cedula del cliente: ')
    estado_civil = comprobar_str('''Seleccione el estado civil del cliente:
    C. Casado
    S. Soltero
    D. Divorciado
    -> ''')
    while not(estado_civil.capitalize() == 'C' or estado_civil.capitalize() == 'S' or estado_civil.capitalize() == 'D'):
        estado_civil = comprobar_str('Error, seleccione un estado existente: ')
    
    tipo_cuenta = comprobar_opcion('''Seleccione que tipo de cuenta desea abrir el cliente:
    1. Corriente
    2. Ahorro
    -> ''', 2)
    
    num_cuenta = generar_num_cuenta()
    
    if tipo_cuenta == 1:
        chequeras = comprobar_num('Ingrese la cantidad de chequeras que desea el cliente: ')

        nueva_cuenta = CuentaCorriente(num_cuenta, 0, chequeras)
    
    else:
        interes = hallar_interes()

        nueva_cuenta = CuentaAhorro(num_cuenta, 0, interes)
    
    nuevo_cliente = Cliente(nombre, cedula, estado_civil, nueva_cuenta)
    return nuevo_cliente

def buscar_cliente(cedula, clientes, i = 0):
    
    if i < len(clientes):
        if clientes[i].cedula == cedula:
            return clientes[i]
    elif i == len(clientes):
        return None
    else:
        return buscar_cliente(cedula, clientes, i + 1)

def imprimir_factura(cliente, operacion, dinero):
    cliente.imprimir_cliente()
    print(f'''Tipo de cuenta: {cliente.cuenta.tipo_cuenta}
    Tipo de operacion: {operacion}
    Monto de operacion: {dinero}
    Saldo final: {cliente.cuenta.saldo}''')

def imprimir_estadisticas(regalado, total_depositado, total_retirado, cont_oper, cont_clientes):
    print(f'''Total depositado: {regalado}
                Total regalado por banco: {total_depositado}
                Total retirado: {total_retirado}
                Cantidad de operaciones: {cont_oper}
                Cantidad clientes registrados: {cont_clientes}''')
    
    
