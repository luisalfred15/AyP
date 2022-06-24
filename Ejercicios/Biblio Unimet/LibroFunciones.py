from Libro_ import Libro
from funciones import *

def añadir_libro(db_libros):
    titulo = comprobar_str('Ingrese el titulo del libro: ')
    edicion = comprobar_str('Ingrese la edicion del libro: ')
    categoria = comprobar_str('Ingrese la categoria del libro: ')
    autores = comprobar_str('Ingrese los autores del libro: ')
    ejemplares = comprobar_num('Ingrese la cantidad de ejemplares que tiene el libro: ')

    nuevo_libro = Libro(titulo, edicion, categoria, autores, ejemplares)
    db_libros.append(nuevo_libro)

def imprimir_libros(db_libros):
    