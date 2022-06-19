from funciones import *
from JuntaDirectiva_ import JuntaDirectiva
from JuntaDirectivaGeneral_ import JuntaDirectivaGeneral
from JuntaDirectivaEscuela_ import JuntaDirectivaEscuela
from Plancha_ import Plancha

planchas = [
  {
    "nombre": "Victor",
    "numero": 10
  },
  {
    "nombre": "Joel",
    "numero": 15
  }
]

jds = [
  {
    "tipo": "G",
    "plancha": 10,
    "presidente": "Mark Del Figgalo",
    "coordinador general": "Patrick Star",
    "tesorero": "Megan Parker",
    "sg": "Helga Pataki",
    "sai": "Josh Nichols"
  },
  {
    "tipo": "G",
    "plancha": 15,
    "presidente": "Sharpay Evans",
    "coordinador general": "Mike Wazowski",
    "tesorero": "London Tipton",
    "sg": "Justin Russo",
    "sai": "Piglet"
  },
  {
    "tipo": "E",
    "plancha": 10,
    "escuela": "Economía",
    "presidente": "Danny Phantom",
    "coordinador general": "Angelica Pickles",
    "tesorero": "Mr. Krabs"
  },
  {
    "tipo": "E",
    "plancha": 10,
    "escuela": "Sistemas",
    "presidente": "Nevel Papperman",
    "coordinador general": "AJ",
    "tesorero": "Sandy Cheeks"
  },
  {
    "tipo": "E",
    "plancha": 10,
    "escuela": "Liberales",
    "presidente": "Fred Figglehorn",
    "coordinador general": "Tootie",
    "tesorero": "Trina Vega"
  },
  {
    "tipo": "E",
    "plancha": 15,
    "escuela": "Economía",
    "presidente": "Kuzco",
    "coordinador general": "Teddy Duncan",
    "tesorero": "Max Russo"
  },
  {
    "tipo": "E",
    "plancha": 15,
    "escuela": "Sistemas",
    "presidente": "Gus Griswald",
    "coordinador general": "Ferb Fletcher",
    "tesorero": "Lizzie McGuire"
  },
  {
    "tipo": "E",
    "plancha": 15,
    "escuela": "Liberales",
    "presidente": "Randall Weems",
    "coordinador general": "Kronk",
    "tesorero": "PJ Duncan"
  },
]

def main():
  print('Benvenido al sistema del FCE!')
  lista_planchas = []
  lista_jd = []
  
  while True:
  
    
    opcion = comprobar_opcion('''Seleccione la opcion deseada:
    1. Registrar planchas
    2. Registrar Juntas Directivas
    3. Ver la informacion de las planchas con sus Juntas Directivas
    4. Generar resultados
    5. Salir del programa
    -> ''', 5)

    if opcion == '1':

      for elemento in planchas:
        nueva_plancha = Plancha(elemento.get('nombre'), elemento.get('numero'))

      lista_planchas.append(nueva_plancha)
        
      print('Planchas registradas con exito')
    
    elif opcion == '2':

      for elemento_2 in jds:
        if elemento_2.get('tipo') == 'G':
          nueva_jd = JuntaDirectivaGeneral('G', elemento_2.get('numero'), elemento_2.get('coordinador general'), elemento_2.get('tesorero'), elemento_2.get('sg'), elemento_2.get('sai'))
        elif elemento_2 == 'E':
          nueva_jd = JuntaDirectivaEscuela('E', elemento_2.get('numero'), elemento_2.get('presidente'), elemento_2.get('coordinador general'), elemento_2.get('tesorero'), elemento_2.get('escuela'))
        
        lista_jd.append(nueva_jd)

      print('Juntas Directivas agregadas con exito')
    
    elif opcion == '3':
      for plancha in lista_planchas:
        plancha.imprimir_plancha()
        for jd in lista_jd:
          if jd.numero_plancha == 10 and jd.tipo == 'G':
            jd.imprimir_jdg()
          elif jd.numero_plancha == 10 and jd.tipo == 'E':
            jd.imprimir_jde()
          elif jd.numero_plancha == 15 and jd.tipo == 'G':
            jd.imprimir_jdg()
          elif jd.numero_plancha == 15 and jd.tipo == 'E':
            jd.imprimir_jde()











main()