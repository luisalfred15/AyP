def sumatoria(numero):
    if numero != 1:
        return numero + sumatoria(numero - 1)
    else:
        return 1

print(sumatoria(5))