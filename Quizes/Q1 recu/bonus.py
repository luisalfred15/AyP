contraseña = input('Ingrese la contraseña: ')

contraseña_valida = True

if len(contraseña) < 8:
    contraseña_valida = False

if contraseña.isalnum() and (contraseña.isupper() or contraseña.islower()) and contraseña.count('_') == 0 and contraseña.count('$') == 0 and contraseña.count('%') == 0:
    contraseña_valida = False

if contraseña.count(' ') == 1:
    contraseña_valida = False

if contraseña_valida:
    print('Contraseña ingresada exitosamente')
else:
    print('La contraseña elegida no es válida')