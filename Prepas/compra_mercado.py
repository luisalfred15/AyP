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
        4: Imprimir todas las facturas
        5: Salir de la base de datos
        -> ''')
    
    if opcion.isnumeric() and 1 <= int(opcion) <= 5:
        if opcion == '1':
            total = 0
            productos_comprados = []
            nombre = input('Ingrese su nombre: ')
            while not(nombre.isalpha()):
                nombre = input('Ingrese un nombre valido: ')
            apellido = input('Ingrese su apellido: ')
            while not(apellido.isalpha()):
                apellido = input('Ingrese un apellido valido: ')
            cedula = input('Ingrese su cedula: ')
            while not(cedula.isnumeric() and int(cedula) > 0):
                nombre = input('Ingrese un numero de cedula valido: ')
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
                'client': {
                    'name': nombre,
                    'last_name': apellido,
                    'id': cedula  
                },
                'date': fecha,
                'bill': {
                    'date': fecha,
                    'products': productos_comprados,
                    'total': total
                }
            }
        elif opcion == '2':
            if len(facturas) != 0:
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
                print('No se pueden eliminar clientes: no hay clientes existentes')  
        elif opcion == '3':
            opcion_agregar = 'S'
            while opcion_agregar == 'S':
                producto_agregado = input('Por favor, introduzca el nombre del producto: ')
                precio_agregado = input('Por favor, introduzca el precio del nuevo producto: ')
                cantidad_agregado = input('Por favor, introduzca la cantidad del nuevo producto: ')
                productos_almacen = len(productos) + 1
                productos[productos_almacen] = {
                    'name': producto_agregado,
                    'amount': int(cantidad_agregado),
                    'price': int(precio_agregado)
                }
                opcion_agregar = input('Desea agregar otro producto? \n S: Si \n N: No \n ->').upper()
        elif opcion == '4':
            print(facturas)
            for key, value in facturas.items():
                print(f'''{key} - {value['client']['name']} {value['client']['last_name']}
                                            Cedula: {value['client']['id']}
                                            Fecha de la compra: {value['date']}
                                            Factura:
                                            - Fecha: {value['bill']['date']}
                                            - Productos: {value['bill']['products']}
                                            - Total: {value['bill']['total']}''')
            break
        else:
            break
    else:
        print('Por favor, ingrese una opcion valida')

# 18/05/2022