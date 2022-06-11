def main():
    base = input('Por favor, ingrese una base: ')
    while not(base.isnumeric()):
        base = input('Por favor, ingrese una base valida: ')
    exponente = input('Por favor, ingrese el exponente deseado: ')
    while not(exponente.isnumeric()):
        exponente = input('Por favor, ingrese un exponente valido: ')
    resultado = exponencial(base, exponente)
    print(resultado)

def exponencial(base, exponente):
    if exponente == 0:
        return 1
    if exponente == 1:
        return base
    return base * exponencial(base, exponente - 1)

main()