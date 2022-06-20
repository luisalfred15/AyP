from Persona_ import *

f = open('G:\Mi unidad\Algoritmos y Programación\En general\Prepas\Persona (manejo arch)\db.txt', 'r') # r de Read para leer el archivo
db = {}

usuarios = f.readlines() # Lee el archivo y genera la lista 'usuarios' que se compone de todas las lineas del archivo
print(usuarios)
for linea in usuarios:
    persona = linea.split(',') # Separa los datos de cada linea (de cada usuario) 
    nueva_persona = Persona(persona[0], persona[1], persona[2])
    db[persona[2]] = nueva_persona
    print(nueva_persona.cedula)