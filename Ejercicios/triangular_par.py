while True:
    b = 0
    comprobado = False
    i = 0
    a = input('Ingrese un numero para averiguar si es par y triangular: ')
    if a.isnumeric() and int(a) > 0:
        while i <= int(a) and not(comprobado):
            while b != int(a) or b > int(a):
                b += 1
            if b == int(a) and int(a) % 2 == 0:
                print('El numero es triangular y par')
                comprobado = True
            else:
                print('El numero o NO es triangular o NO es par')
                comprobado = True
    elif a.isnumeric() and int(a) == 0:
        break
    else:
        print('Introduzca un valor valido')