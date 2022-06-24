import pickle
import os
import requests

# Para obtener los datos del JSON

def get_json():
    r = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2122-3/saman_fifa_api/main/api.json')
    if r.status_code == 200:
        db = r.json()
    return db

# Para cargar los datos a archivos de texto

def load_data(txt):
    file = open(txt, 'rb')
    if os.stat(txt).st_size != 0:
        file.seek(0)
        data = pickle.load(file)
    file.close()
    return data

def load_empty_data(txt):
    file = open(txt, 'rb')
    try:
        data = pickle.load(file)
    except EOFError:
        data = []
    file.close()
    return data

# Comprobaciones

def comprobar_str(msg):
    string = input(msg)
    if string.replace(' ', '').replace('.', '').isalpha():
        return string
    else:    
        return comprobar_str('Error, ingrese palabras validas: ')

def comprobar_opcion(msg, cantidad_opciones):
    opcion = input(msg)
    if opcion.isnumeric() and int(opcion) in range(1, cantidad_opciones + 1):
        return opcion
    else:
        return comprobar_opcion('Error, seleccione una opcion que este dentro del rango: ', cantidad_opciones)

def comprobar_num(msg):
    num = input(msg)
    if num.isnumeric() and 0 < int(num):
        return num
    else:
        return comprobar_num('Error, ingrese un numero valido: ')