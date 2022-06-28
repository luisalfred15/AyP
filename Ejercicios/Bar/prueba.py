def edad_es_fibo(f0, f1, edad):
    resultado = f0 + f1
    edadEsFibo = False
    if resultado < edad:
        return edad_es_fibo(f1, resultado, edad)
    elif resultado == edad:
        edadEsFibo = True
        return edadEsFibo
    else:
        return edadEsFibo

edadEsFibo = edad_es_fibo(0, 1, 20)

if edadEsFibo:
    print('Edad pertenece a Fibonacci')
else:
    print('Edad no pertenece a Fibonacci')