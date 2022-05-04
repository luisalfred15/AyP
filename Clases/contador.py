print('**** Bienvenido ****')

numero = int(input('Ingrese un numero: '))
i = numero

if numero >= 0:
    while i >= 0:
        if i == 0: # Si llega al 0, lo imprime sin la coma
            print(i)
            i -= 1
        else:
            print(i,end=', ')
            i -= 1 # Importante las variables de control para no producir bucle infinito
else:
    print('Introduzca un valor valido')
