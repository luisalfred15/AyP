# Busq lineal: va comparando elemento a elemento hasta hallarlo
# Busq binaria: separa la lista en dos. Si 

def main():
    lista = [3, 5, 7, 1, 4, 8, 9, 2, 6]
    number = int(input('Ingresa el numero que deseas buscar: '))
    print(linear_search(lista, number))

def linear_search(lista, number_to_find):
    for num in lista:
        if num == number_to_find:
            return f'The number {number_to_find} is in the list'
    return -1                       # Siempre cuando no se encuentra la opcion, se retorna -1

main()