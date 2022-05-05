numero = int(input('Ingrese el numero para averiguar si es primo: '))
i = numero

while i < numero:
    division = numero / i
    if division.is_integer() and (numero == i or i == 1):
        print('El ', numero, 'es primo')
    else:
        print('El ', numero, 'NO es primo')
    i += 1