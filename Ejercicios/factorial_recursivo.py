def hallar_factorial(numero):
    if numero != 1:
        return numero * hallar_factorial(numero - 1)
    else:
        return 1

resultado = hallar_factorial(5)
print(resultado)