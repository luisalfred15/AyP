
def determinar_incremental(numero, i = 0):
    if numero[i] < numero[i + 1]:
        return determinar_incremental(numero[i:])
    else:
        return False

def main():

    numero = input('Ingrese un numero: ')

    # for i in range(len(numero) - 1):
    #     if numero[i] < numero[i + 1]:
    #         es_incremental = True
    #     else:
    #         es_incremental = False
    #         break

    es_incremental = determinar_incremental(numero)    




    if es_incremental:
        print('El numero es incremental')
    else:
        print('El numero NO es incremental')