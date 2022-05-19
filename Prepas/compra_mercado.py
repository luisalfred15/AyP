facturas = {}
productos = {
    1: {
        "name":"Dorito",
        "amount": 100,
        "price": 6,
    },
    2: {
        "name":"Pirulin",
        "amount": 100,
        "price": 7,
    },
    3: {
        "name":"Rufles",
        "amount": 100,
        "price": 2,
    },
    4: {
        "name":"Pepito",
        "amount": 100,
        "price": 4,
    }
}

numero_comprador = 0

print('Bienvenido a Farmatodo!')

while True:
    opcion = input('''Por favor, seleccione una opcion:
        1: Agregar un cliente a la base de datos
        2: Eliminar un cliente de la base de datos
        3: Agregar un producto al almacen
        4: Salir de la base de datos
        -> ''')
    
    if opcion.isnumeric() and 1 <= int(opcion) <= 4:
        if opcion == '1':
            total = 0
            productos_comprados = []
            nombre = input('Ingrese su nombre: ')
            apellido = input('Ingrese su apellido: ')
            cedula = input('Ingrese su cedula: ')
            fecha = input('Ingrese la fecha de la compra en el formato dd/mm/aaaa: ')
            while True:
                for key, value in productos.items():
                    print(f'''{key} - {value['name']}
                                        Cantidad: {value['amount']}
                                        Precio: {value['price']}''')
                opcion_compra = input('Selecciona el producto que deseas agregar a la factura. De lo contrario, selecciona 0: ')
                if opcion_compra.isnumeric() and int(opcion_compra) != 0:
                    while not(int(opcion_compra) <= len(productos)):
                        opcion_compra = input('Por favor, seleccione un producto que este enlistado arriba: ')
                    productos_comprados.append(productos[int(opcion_compra)]['name'])
                    cantidad_compra = input('Seleccione la cantidad del producto que desea adquirir: ')
                    while not(int(cantidad_compra) <= productos[int(opcion_compra)]['amount']):
                        cantidad_compra = input('Por favor, introduce una cantidad que no sobrepase el stock: ')
                    total += productos[int(opcion_compra)]['price'] * int(cantidad_compra)
                    productos[int(opcion_compra)]['amount'] -= int(cantidad_compra)
                elif opcion_compra.isnumeric() and int(opcion_compra) == 0:
                    break
            numero_comprador += 1
            facturas[int(numero_comprador)] = {
                'name': nombre,
                'last_name': apellido,
                'id': cedula,
                'date': fecha,
                'bill': {
                    'date': fecha,
                    'products': productos_comprados,
                    'total': total
                }
            }
        elif opcion == '2':
            for key, value in facturas.items():
                    print(f'''{key} - {value['name']} {value['last_name']}
                                        Cedula: {value['id']}
                                        Fecha de la compra: {value['date']}
                                        Factura:
                                        - Fecha: {value['bill']['date']}
                                        - Productos: {value['bill']['products']}
                                        - Total: {value['bill']['total']}''')
            eliminado = input('Seleccione el que desee eliminar de la base de datos: ')
            while not(eliminado.isnumeric() and 1 <= int(eliminado) <= len(facturas)):
                eliminado = input('Por favor, seleccione un cliente existente: ')
            facturas.pop(int(eliminado))  
        else:
            print(facturas)
            break
    else:
        print('Por favor, ingrese una opcion valida')

# 18/05/2022