db = {}
monto = 40
contador_viajeros = 1
print('Bienvenido a Transportes Unimet!')

while True:
    descuento = 0
    es_incremental = False
    total = 0
    opcion = input('''Ingrese la opcion deseada:
    1. Agregar un viajero
    2. Eliminar un viajero
    3. Imprimir todos los viajeros
    4. Salir de la base de datos
    -> ''')
    if opcion.isnumeric() and 1 <= int(opcion) <= 4:
        if opcion == '1':
            nombre = input('Ingrese el nombre del viajero: ')
            while not(nombre.isalpha()):
                nombre = input('Ingrese un nombre valido: ')
            apellido = input('Ingrese el apellido del viajero: ')
            while not(apellido.isalpha()):
                apellido = input('Ingrese un apellido valido: ')
            edad = input('Ingrese la edad del viajero: ')
            while not(edad.isnumeric() and int(edad) > 0):
                edad = input('Ingrese una edad valida: ')
            cedula = input('Ingrese la cedula del viajero: ')
            while not(cedula.isnumeric() and int(cedula) > 0):
                cedula = input('Ingrese una cedula valida: ')

            if int(edad) > 55:
                descuento += monto * 0.4
                descuento_edad = 'Si'
            else:
                descuento_edad = 'No'

            if int(cedula[-1])>int(cedula[-2])>int(cedula[-3]):
                es_incremental = True
            
            if es_incremental:
                descuento += 0.3
                descuento_cedula = 'Si'
            else:
                descuento_cedula = 'No'
            
            total = monto - descuento

            db[contador_viajeros] = {
                'nombre': nombre,
                'apellido': apellido,
                'edad': edad,
                'cedula': cedula,
                'monto': 40,
                'descuento_cedula': descuento_cedula,
                'descuento_edad': descuento_edad,
                'total': total
            }

            contador_viajeros += 1
        
        elif opcion == '2':
            print('             *** VIAJEROS ***')
            for key, value in db.items():
                print(f'''              {key}: {value.get('nombre')} {value.get('apellido')}
                Edad: {value.get('edad')}
                Cedula: {value.get('cedula')}
                Total: {value.get('total')}''')
            
            eleccion = input('Ingrese el numero del viajero que desee eliminar: ')
            while not(eleccion.isnumeric() and 0 < int(eleccion) < contador_viajeros):
                eleccion = input('Ingrese un numero valido de viajero: ')

            db.pop(int(eleccion))
        
        elif opcion == '3':
            print('             *** VIAJEROS ***')
            for key_2, value_2 in db.items():
                print(f'''              {key_2}: {value_2.get('nombre')} {value_2.get('apellido')}
                Edad: {value_2.get('edad')}
                Cedula: {value_2.get('cedula')}
                Monto: {value_2.get('monto')}
                Descento de edad: {value_2.get('descuento_edad')}
                Descuento de cedula: {value_2.get('descuento_cedula')}
                Total: {value_2.get('total')}''')

        elif opcion == '4':
            break
    else:
        print('Ingrese una opcion valida')