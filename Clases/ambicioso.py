numero = int(input('Ingrese un numero: '))
acum_numero = 0
acum_perfecto = 0

for i in range(1,numero):
    if numero % i == 0:
        acum_numero = acum_numero + i

for j in range(1,acum_numero):
    if acum_numero % j == 0:
        acum_perfecto = acum_perfecto + j

if acum_perfecto == acum_numero:
    print(numero,'es ambicioso')
else:
    print(numero,'no es ambicioso')