numero = input('Ingrese el numero. Luego presione Enter para saber si es incremental: ')

if numero.isnumeric() and len(numero) == 3:
    if int(numero[0])<int(numero[1])<int(numero[2]):
        print('El numero es incremental')
    else:
        print('El numero NO es incremental')
else:
    print('Ingrese un numero valido')