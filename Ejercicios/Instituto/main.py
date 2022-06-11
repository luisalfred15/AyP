from Alumnos_ import Alumno

def main():
    
    contador = 1
    db = {}
    anadir_alumnos = 'S'
    promedios = []
    i = 0
    j = 0

    while True:
        print('Bienvenido al Insti!')
        while anadir_alumnos.capitalize() == 'S': 
            nombre = input('Por favor, ingrese el nombre del alumno: ')
            while not(nombre.isalpha()):
                nombre = input('Por favor, ingrese un nombre valido: ')
            grado = input('Por favor, ingrese el grado del alumno: ')
            while not(grado.isnumeric() and int(grado) > 0):
                grado = input('Por favor, ingrese un grado valido: ')
            promedio = input('Por favor, ingrese el promedio del alumno: ')
            while not(promedio.isnumeric() and int(promedio) >= 0):
                promedio = input('Por favor, ingrese un promedio valido: ')
            direccion = input('Por favor, ingrese la direccion del alumno: ')
            while not(direccion.isalpha()):
                direccion = input('Por favor, ingrese una direccion valido: ')
            nombre_representante = input('Por favor, ingrese el nombre del representante del alumno: ')
            while not(nombre_representante.isalpha()):
                nombre_representante = input('Por favor, ingrese un nombre de representante valido: ')
            telefono_representante = input('Por favor, ingrese el telefono del representante del alumno: ')
            while not(telefono_representante.isnumeric() and int(telefono_representante) > 0):
                telefono_representante = input('Por favor, ingrese un telefono de representante valido: ')

            promedios.append(int(promedio))
            
            alumno = Alumno(nombre, grado, promedio, direccion, nombre_representante, telefono_representante)
            becado = alumno.esBecado(promedio)

            db[contador] = { # Al usar diccionarios, se mezcla con problema de BD. Se pueden aprovechar mejor las funciones de objetos
                'nombre': nombre,
                'grado': grado,
                'promedio': promedio,
                'direccion': direccion,
                'nombre_representante': nombre_representante,
                'telefono_representante': telefono_representante,
                'becado': becado,
            }

            contador += 1

            anadir_alumnos = input('''Desea añadir otro alumno a la base de datos?
            S: Si
            N: No
            -> ''')
        
        imprimir_alumnado(db)
        media = media_promedios(promedios, i)
        print(f'Promedio del alumnado: {media}')
        conteo_promedios = contar_promedios(promedios, j)
        imprimir_estadisticas(conteo_promedios)
        break

def imprimir_alumnado(db):
    print('     **** ALUMNADO ****')
    for key, value in db.items():
        print(f'''{key}: {value.get('nombre')}
        Grado: {value.get('grado')}
        Promedio: {value.get('promedio')}
        Direccion: {value.get('direccion')}
        Nombre del representante: {value.get('nombre_representante')}
        Telefono del representante: {value.get('telefono_representante')}
        Condicion de beca: {value.get('becado')}''')

def media_promedios(promedios, i):
    acumulador = 0
    while i < len(promedios):
        acumulador += promedios[i]
        i += 1
    return acumulador / 2

def contar_promedios(promedios, j):
    contador_1 = 0
    contador_2 = 0
    contador_3 = 0
    while j < len(promedios):
        if promedios[j] < 10:
            contador_1 += 1
        elif 10 <= promedios[j] < 16:
            contador_2 += 1
        elif promedios[j] >= 16:
            contador_3 += 1
        j += 1
    return (contador_1, contador_2, contador_3)

def imprimir_estadisticas(conteo_promedios):
    print(f'''      *** PROMEDIOS GENERALES ***
    Menores que 10: {conteo_promedios[0]}
    Entre 10 y 16: {conteo_promedios[1]}
    Mayores que 16: {conteo_promedios[2]}''')

main()