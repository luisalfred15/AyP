from Participante_ import Participante
from Cantante_ import Cantante
from Bailarin_ import Bailarin
from Musico_ import Musico
from Libre_ import Libre
from funicones import *

opciones_formato = {'1': 'Solista', '2': 'Grupo'}
opciones_categoria = {'1': 'Canto', '2': 'Baile', '3': 'Musica', '4': 'Libre'}

def main():
    
    print('Bienvenido al Got Talent Show!')
    formato = comprobar_opcion('''Ingrese si actuara en grupo o solista: 
    1. Solista
    2. Grupo
    -> ''', 2)
    if formato == '1':
        nombre = comprobar_str('Introduce el nombre del participante: ')
    else:
        nombre = comprobar_str('Introduce el nombre del grupo: ')
    categoria = comprobar_opcion('''Seleccione la categoria en la que participara:
    1: Canto
    2: Baile
    3: Musica
    4: Libre
    -> ''', 4)
    telefono = comprobar_num('Ingrese un numero de telefono: ')
    registro = comprobar_num('Ingrese el numero de registro del participante: ')

    participante = Participante(nombre, opciones_formato.get(formato), opciones_categoria.get(categoria), telefono, registro)
    
    if categoria == '1':
        cancion = comprobar_str('Ingrese la cancion que interpretara: ')
        autor = comprobar_str('Ingrese el autor de la cancion: ')
        participante = Cantante(nombre, opciones_formato.get(formato), opciones_categoria.get(categoria), telefono, registro, cancion, autor)
    
    elif categoria == '2':
        estilo = comprobar_str('Ingrese el estilo que interpretara: ')
        participante = Bailarin(nombre, opciones_formato.get(formato), opciones_categoria.get(categoria), telefono, registro, estilo)
    
    elif categoria == '3':
        instrumentos = []
        opcion = '1'
        while opcion == '1':
            instrumento = comprobar_str('Ingrese el instrumento que interpretara: ')
            instrumentos.append(instrumento)
            opcion = comprobar_opcion('''Desea agregar otro instrumento?
            1: Si
            2: No
            -> ''', 2)
        participante = Musico(nombre, opciones_formato.get(formato), opciones_categoria.get(categoria), telefono, registro, instrumentos)
    
    elif categoria == '4':
        libre = comprobar_str('Ingrese el talento del participante: ')
        participante = Libre(nombre, opciones_formato.get(formato), opciones_categoria.get(categoria), telefono, registro, libre)

    participante.imprimir_concursante()
    participante.imprimir_otros()





main()