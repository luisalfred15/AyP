entrada = input('Ingrese un numero positivo o palabra: ') # Se toma la entrada como string
i = 0
datos_iguales = True

while i <= len(entrada) // 2:
    dato_1 = entrada[-len(entrada)+i]
    dato_2 = entrada[len(entrada)-i-1]
    if dato_1 != dato_2:
        datos_iguales = False
    i += 1

if datos_iguales:
    if entrada.isnumeric():
        print('El numero ingresado es un palindromo')
    else:
        print('La palabra ingresada es un palindromo')
else:
    if entrada.isnumeric():
        print('El numero ingresado NO es un palindromo')
    else:
        print('La palabra ingresada NO es un palindromo')

# Solucion alterna

# if entrada == entrada[::-1]: # Voltea el string
#     print(entrada, 'es un palindromo')
# else:
#     print(entrada, 'no es un palindromo')