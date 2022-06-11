def main():
    palabra = ('Por favor, ingrese una palabra: ')
    invertir_palabra(palabra)

def invertir_palabra(palabra):
    letra = 0
    if letra > len(palabra) // 2:
        palabra[letra] = palabra[-letra]
    return invertir_palabra


main()