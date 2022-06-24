from BebidaAlcoholica_ import BebidaAlcoholica
from BebidaNoAlcoholica_ import BebidaNoAlcoholica
from Cliente_ import Cliente

def comprobar_str(msg):
    string = input(msg)
    if string.replace(' ', '').isalpha():
        return string
    else:    
        return comprobar_str('Error, ingrese palabras validas: ')

def comprobar_opcion(msg, cantidad_opciones):
    opcion = input(msg)
    if opcion.isnumeric() and int(opcion) in range(1, cantidad_opciones + 1):
        return opcion
    else:
        return comprobar_opcion('Error, seleccione una opcion que este dentro del rango: ', cantidad_opciones)

def comprobar_num(msg):
    num = input(msg)
    if num.isnumeric() and 0 <= int(num):
        return num
    else:
        return comprobar_num('Error, ingrese un numero valido: ')

def comprobar_fecha(msg):
    fecha = input(msg)
    if fecha.replace('/', '').isnumeric():
        return fecha
    else:
        return comprobar_fecha('Error, ingrese una fecha valida: ')

def añadir_beb_alco(bebidas_alco):
    nombre_beb = comprobar_str('Ingrese el nombre de la bebida: ')
    precio_beb = comprobar_num('Ingrese el precio de la bebida: ')
    grado_beb = comprobar_num('Ingrese el grado alcoholico de la bebida: ')
    nueva_bebida = BebidaAlcoholica(nombre_beb, precio_beb, grado_beb)
    bebidas_alco.append(nueva_bebida)
    return bebidas_alco

def añadir_beb_no_alco(bebidas_no_alco):
    nombre_beb = comprobar_str('Ingrese el nombre de la bebida: ')
    precio_beb = comprobar_num('Ingrese el precio de la bebida: ')
    temp = comprobar_num('Ingrese la temperatura de la bebida: ')
    nueva_bebida = BebidaNoAlcoholica(nombre_beb, precio_beb, temp)
    bebidas_no_alco.append(nueva_bebida)
    return bebidas_no_alco

def añadir_cliente(clientes):
    nombre_cliente = comprobar_str('Ingrese el nombre del cliente: ')
    cedula_cliente = comprobar_num('Ingrese la cedula del cliente: ')
    edad_cliente = comprobar_num('Ingrese la edad del cliente: ')
    nuevo_cliente = Cliente(nombre_cliente, cedula_cliente, edad_cliente)
    clientes.append(nuevo_cliente)
    return clientes