abecedario = list(input('Introduza el abecedario a reducir: '))
i = 1

while i < len(abecedario):
    if i % 3 == 0:
        abecedario.pop(i)
        i += 1
    else:
        abecedario.append(i)
        i += 1

print('El abecedario es:',abecedario)