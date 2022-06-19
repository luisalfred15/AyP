import requests
import json
import pickle
import os

def get_json():
    response = requests.get('https://raw.githubusercontent.com/Algoritmos-y-Programacion-2122-3/saman_fifa_api/main/api.json')
    if response.status_code == 200:
        db = response.json()
        print(type(db))
    return db

def load_data(txt):
    file = open(txt, )