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
        data = pickle.load(file)
    file.close()
    return data