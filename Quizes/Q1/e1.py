es_repunit = False
aux = 0
es_cuadrado = False

numero = input('Por favor, ingrese un numero para verificar si es Repunit y cuadrado: ')

num_prueba = numero[0]

if numero.count(num_prueba) == len(numero):
    es_repunit = True

for i in range(len(numero)):
    aux_num = int(numero[i])
    aux += aux_num

for j in range(1, aux + 1):
    if aux == j ** 2:
        es_cuadrado = True

if es_repunit and es_cuadrado:
    print('El numero ingresado es Repunit y cuadrado')
else:
    print('El numero o NO es Repunit o NO es cuadrado')