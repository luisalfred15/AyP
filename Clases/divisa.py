divisas = {'Euro':'E', 'Dolar': '$', 'Yen': 'Y'}
divisa_seleccionada = input('Ingrese la divisa a consultar: ')

# if divisa_seleccionada in divisas:
#     print('El simbolo es', divisas[divisa_seleccionada])
# else:
#     print('La divisa no se encuentra en el diccionario')

# Solucion alterna

print(divisas.get(divisa_seleccionada, 'La divisa no se encuentra en el diccionario'))