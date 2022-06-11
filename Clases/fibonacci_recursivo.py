def main():
    limite = int(input('Por favor, ingrese el limite de la sucesion de Fibonacci: '))
    num_1 = 0
    num_2 = 1
    resultado = hallar_sucesion(num_1, num_2, limite)
    
    

def hallar_sucesion(num_1, num_2, limite):
    print(num_1, end = ' ')
    if limite == 1:
        return num_1
    return hallar_sucesion(num_2, num_1 + num_2, limite - 1)


main()