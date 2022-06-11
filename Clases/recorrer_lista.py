def main():
    lista = [1, 2, 3, 4, 5, 6, 7]
    elemento = int(input('Ingrese el elemento que desea buscar: '))
    i = len(lista) - 1
    print(recorrer_lista(lista, elemento, i))




def recorrer_lista(lista, elemento, i):
    elemnto_hallado = False
    if lista[i] == elemento and elemento_hallado:
        return "Elemento hallado" and 
    elif lista[i] == len(lista) - 1:
        return "No se hallo el elemento"
    return recorrer_lista(lista, elemento, i - 1)





main()