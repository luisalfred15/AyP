# Funcion recibe lista desordenada
# Saca el elemento mayor
# Lo aniade a la lista que va a estar ordenada
# Se elimina el elemento mayor de la lista original
# Funcion retorna ella misma con lista sin elemento mayor
# Condicion de salida: longitud de la lista desordenada

# Para indices negativos

def ordenar_lista(lista, lista_ordenada, indice):
    num_may = 0
    for elemento in lista:
        if elemento > num_may:
            num_may = elemento
    lista_ordenada.insert(indice, num_may)
    lista.pop(lista.index(num_may))
    if len(lista) != 0:
        return ordenar_lista(lista, lista_ordenada, indice - 1)
    else:
        return lista_ordenada

lista_final = ordenar_lista([7, 1, 3, 5, 4, 0, 25], [], -1)
print(lista_final)

# Para indices positivos

def ordenar_lista(lista, lista_ordenada, indice):
    num_may = 0                                         # Se establece como numero mayor al 0 para buscar el mayor real y comenzar la comparacion
    for elemento in lista:
        if elemento > num_may:                          # Si se halla un elemento mayor al numero mayor, 
            num_may = elemento                          # ese elemento sera ahora el numero mayor
    lista_ordenada.insert(indice, num_may)              # El numero se aniade a la lista ordenada en el indice deseado (0 porque se quiere ascendente)
    lista.pop(lista.index(num_may))                     # Se elimina de la lista original al numero mayor para aplicar la recursividad
    if len(lista) != 0:                                             # Cond. de salida: longitud de la lista. Cuando no hayan elementos en la lista original, se detiene la recursividad
        return ordenar_lista(lista, lista_ordenada, indice)
    else:
        return lista_ordenada

lista_final = ordenar_lista([7, 1, 3, 5, 4, 0, 25], [], 0) # Nota: se puede omitir el argumento indice
print(lista_final) # Imprime la lista ordenada ascendentemente. Para descendentemente, sustituir insert por apend en l32