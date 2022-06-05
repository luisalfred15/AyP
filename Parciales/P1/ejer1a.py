comando = input('Por favor, ingrese el comando: ')

def convertidor_goal(comando):
    com_1 = comando.replace('()','o')
    com_final = com_1.replace('(al)', 'al')
    return print(com_final)

convertidor_goal(comando)