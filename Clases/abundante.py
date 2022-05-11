numero = int(input('Ingrese un numero: '))
suma_divisores = 0

for i in range(1,numero):
    if numero % i == 0:
        suma_divisores = suma_divisores + i

if suma_divisores > numero:
    print('El numero es abundante')
else:
    print('El numero NO es abundante')