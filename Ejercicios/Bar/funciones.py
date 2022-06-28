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

def generar_beb_alco():
        
    nombre = comprobar_str('Ingrese el nombre de la bebida: ')
    precio = comprobar_num('Ingrese el precio de la bebida: ')
    precio = int(precio)
    grado = comprobar_num('Ingrese el grado alcoholico de la bebida: ')

    nueva_bebida_alco = BebidaAlcoholica(nombre, precio, 'A', grado)

    return nueva_bebida_alco

def generar_beb_no_alco():
        
    nombre = comprobar_str('Ingrese el nombre de la bebida: ')
    precio = comprobar_num('Ingrese el precio de la bebida: ')
    precio = int(precio)
    temp = comprobar_num('Ingrese la temperatura a la que debe ser mantenida la bebida: ')

    nueva_bebida_no_alco = BebidaNoAlcoholica(nombre, precio, 'NA', temp)

    return nueva_bebida_no_alco

def generar_cliente():

    nombre = comprobar_str('Ingrese el nombre del cliente: ')
    edad = comprobar_num('Ingrese la edad del cliente: ')
    edad = int(edad)
    cedula = comprobar_num('Ingrese la cedula del cliente: ')

    nuevo_cliente = Cliente(nombre, edad, cedula)

    return nuevo_cliente

def imprimir_factura(cliente):
    cliente.imprimir_cliente()
    imprimir_pedido(cliente)
    costo = calcular_costo(cliente)
    costoEsPrimo = costo_es_primo(costo)
    edadEsFibo = edad_es_fibo(0, 1, cliente)
    descuento = calcular_descuento(costo, edadEsFibo, costoEsPrimo)
    total = calcular_total(costo, descuento)
    print(f'Total: {total}')

def imprimir_pedido(cliente):
    for bebida in cliente.pedido:
        print(f'''ID: {cliente.pedido.index(bebida) + 1}
        Nombre: {bebida.nombre}
        Precio: {bebida.precio}''')
        if bebida.tipo == 'A':
            print(f'Grado alcoholico: {bebida.grado}')
        else:
            print(f'Temperatura de mantenimiento: {bebida.temp}')

def calcular_total(costo, descuento):
    return costo - descuento

def calcular_descuento(costo, edadEsFibo, costoEsPrimo):
    descuento = 0
    if edadEsFibo:
        descuento += 0.05
    if costoEsPrimo:
        descuento += 0.1
    return costo * descuento

def calcular_costo(cliente):
    costo = 0
    for bebida in cliente.pedido:
        costo += bebida.precio
    return costo

def costo_es_primo(costo):
    divisores = 0
    costoEsPrimo = False
    for i in range(1, costo + 1):
        if costo % i == 0:
            divisores += 1
    if divisores == 2:
        costoEsPrimo = True
    return costoEsPrimo

def edad_es_fibo(f0, f1, cliente):
    resultado = f0 + f1
    edadEsFibo = False
    if resultado < cliente.edad:
        return edad_es_fibo(f1, resultado, cliente)
    elif resultado == cliente.edad:
        edadEsFibo = True
        return edadEsFibo
    else:    
        return edadEsFibo