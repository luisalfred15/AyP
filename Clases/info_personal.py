# nombre = input('Ingrese su nombre: ')
# edad = input('Ingrese su edad: ')
# direccion = input('Ingrese su direccion: ')
# telefono = input('Ingrese su numero telefonico: ')

# datos_personales = {'nombre': nombre, 'edad': edad, 'direccion': direccion, 'telefono': telefono}

# print(datos_personales['nombre'],'tiene',datos_personales['edad'],'años, vive en',datos_personales['direccion'],'y su número de teléfono es',datos_personales['telefono'])

# Solucion alterna

datos_personales = {}
datos_personales['nombre'] = input('Ingrese su nombre: ')
datos_personales['edad'] = input('Ingrese su edad: ')
datos_personales['direccion'] = input('Ingrese su direccion: ')
datos_personales['telefono'] = input('Ingrese su numero telefonico: ')

print(datos_personales.get('nombre'),'tiene',datos_personales.get('edad'),'años, vive en',datos_personales.get('direccion'),'y su número de teléfono es',datos_personales.get('telefono'))