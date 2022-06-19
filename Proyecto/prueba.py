import pickle
import os

def cargar_datos(txt):
    file= open(txt,'rb')
    if os.stat(txt).st_size != 0:
        datos = pickle.load(file)
    file.close()
    return datos

prueba = cargar_datos('Prueba.txt')
print(prueba)

# archivo = open('archivo.txt', 'r')
# datos = archivo.read()
# archivo.close()

# print(datos)