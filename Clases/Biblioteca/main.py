from funciones import *
from Publicacion_ import *
from Libro_ import *
from PublicacionPeriodica_ import *
from MedioAudiovisual_ import *
from Musica_ import *
from Video_ import *

def main():
    historial = []
    print('Bienvenido a la Biblioteca!')
    while True:
        opcion = comprobar_opcion('''Seleccione la opcion deseada:
        1. Agregar una publicacion
        2. Imprimir el historial
        3. Salir del programa
        -> ''', 3)

        if opcion == '1':
            
            nombre = comprobar_str('Ingrese el nombre de la publicacion: ')
            autor = comprobar_str('Ingrese el autor o los autores de la publicacion: ')
            fecha_publicacion = comprobar_fecha('Ingrese la fecha de publicacion: ')
            opcion_publicacion = comprobar_opcion('''Seleccione el tipo de publicacion que desee agregar: 
            1. Libro
            2. De medio audiovisual
            3. Periodica
            -> ''', 3)

            if opcion_publicacion == '1':
                nueva_publicacion = Libro(nombre, autor, fecha_publicacion, 'Libro')


            elif opcion_publicacion == '2':
                opcion_audiovisual = comprobar_opcion('''Seleccione la opcion de la publicacion de medio audiovisual:
                1. Video
                2. Musica
                -> ''', 2)
                if opcion_audiovisual == '1':
                    nueva_publicacion = Video(nombre, autor, fecha_publicacion, 'Video')

                elif opcion_audiovisual == '2':
                    nueva_publicacion = Musica(nombre, autor, fecha_publicacion, 'Musica')

            elif opcion_publicacion == '3':
                nueva_publicacion = PublicacionPeriodica(nombre, autor, fecha_publicacion, 'Publicacion periodica')
            
            nueva_publicacion.agregar_a_historial(historial, nueva_publicacion)

        elif opcion == '2':
            print('*** HISTORIAL ***')
            for key in historial:
                print(f'            --- {historial.index(key) + 1} ---')
                key.imprimir_publicacion()
        
        elif opcion == '3':
            break
        
main()