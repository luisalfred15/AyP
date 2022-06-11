numero = int(input('Ingrese un numero: '))
acum = 0
es_perfecto = False
contador = 1
a = 0
b = 0
es_producto_perfecto = False
lista_perfectos = []

for i in range(1, numero):
    if numero % i == 0:
        aux = i
        for j in range(1, aux):
            if aux % j == 0:
                acum = acum + j
        if aux == acum:
            lista_perfectos.append(aux)


print(lista_perfectos)