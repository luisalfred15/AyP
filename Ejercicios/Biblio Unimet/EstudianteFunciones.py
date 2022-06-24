from Estudiante_ import Estudiante
from funciones import *

def añadir_estudiante(db_estudiantes):
    nombre = comprobar_str('Ingrese el nombre del estudiante: ')
    apellido = comprobar_str('Ingrese el apellido del estudiante: ')
    telefono = comprobar_str('Ingrese el numero de telefono del estudiante: ')
    carnet = comprobar_num('Ingrese el carnet del estudiante: ')
    carrera = comprobar_str('Ingrese la carrera que estudia: ')
    ejemplares = ''

    nuevo_estudiante = Estudiante(nombre, apellido, telefono, carnet, carrera, ejemplares)
    db_estudiantes.append(nuevo_estudiante)