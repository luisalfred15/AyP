print('***** Bienvenido a la calculadora *****')

numero_1 = input('Ingrese el primer numero: \n')
numero_2 = input('Ingrese el segundo numero: \n')

if numero_1.isnumeric() and numero_2.isnumeric():
    operacion = input('Seleccione la operacion a realizar: \n \t 1: Suma \t 2: Resta \t 3: Multiplicacion \t 4: Division \n')
    numero_1 = int(numero_1)
    numero_2 = int(numero_2)
else:
    print('Error: Datos de entrada no acpetados')

if operacion.isnumeric():
    operacion = int(operacion)

if operacion == 1:
    suma = numero_1 + numero_2
    print('El resultado de la suma es ', suma)
elif operacion == 2:
    resta = numero_1 - numero_2
    print('El resultado de la resta es ', resta)
elif operacion == 3:
    multiplicacion = numero_1 * numero_2
    print('El resultado de la multiplicacion es ', multiplicacion)
elif operacion == 4:
    if numero_2 != 0:
        division = numero_1 / numero_2
        print('El resultado de la division es ', division)
    else:
        print('Error: No se pudo realizar la operacion')
else:
    print('Seleccione una de las operaciones enlistadas')