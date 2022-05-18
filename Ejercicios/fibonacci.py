def main():
    numero = int(input('Introduce el numero hasta donde quieras que llegue la sucesion: '))
    fibonacci_inicial = [0, 1]
    sucesion = fibonacci_inicial
    crear_sucesion(numero)
    imprimir_sucesion()

def crear_sucesion(numero):
    for i in range(numero):
        f_nuevo = sucesion[i] + sucesion[i + 1]
        sucesion.append(f_nuevo)

def imprimir_sucesion():
    for j in range(len(sucesion)):
        if j == len(sucesion) - 1:
            print(sucesion[j])
        else:
            print(sucesion[j], end = ', ')

main()