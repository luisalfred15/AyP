figura = input('Ingresa el numero para seleccionar el tipo de figura y luego presiona Enter: \n 1: Circunferencia \n 2: Elipse \n 3: Cuadrado \n 4: Rectangulo \n 5: Triangulo \n 6: Rombo \n')

if figura.isnumeric() and int(figura) >= 1 and int(figura) <= 6:
    if figura == '1':
        radio = input('Ingresa el valor para el radio, luego presiona Enter: ')
        if radio.isnumeric() and radio > 0:
            area = 3.14 * radio ** 2
            print('El area de la circunferencia es ', area)
        else:
            print('Ingresa valores validos')
    elif figura == '2':
        radio_1 = input('Ingresa el valor para el primer radio, luego presiona Enter: ')
        radio_2 = input('Ingresa el valor para el segundo radio, luego presiona Enter: ')
        if (radio_1.isnumeric() and radio_2.isnumeric()) and (radio_1 > 0 and radio_2 > 0):
            area = 3.14 * radio_1 * radio_2
            print('El area de la elipse es ', area)
        else:
            print('Ingresa valores validos')
    else:
        lado = input('Ingresa el valor para el lado, luego presiona Enter: ')
        if lado.isnumeric() and lado > 0:
            area = lado ** 2
            print('El area del cuadrado es ', area)
        else:
            print('Ingresa valores validos')
else:
    print('Ingresa una opcion valida')

# num_1 = '14'
# num_2 = '5'

# if num_1 > num_2:
#     print('Se verifica')
# else:
#     print('No se verifica')