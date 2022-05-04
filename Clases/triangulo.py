filas = int(input('Introduce el numero filas para el triangulo: '))
fila_actual = 1
numero_actual = 1

if filas > 0:
    print(numero_actual)
    while fila_actual < filas:
        numero_actual += 2
        i = numero_actual
        while i > 0:
            if i == 1:
                print(i)
            else:
                print(i,end=' ')
            i -= 2
        fila_actual += 1