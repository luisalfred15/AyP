# numero = int(input('Introduce un numero: '))
# i = 1

# if numero >= 0:
#     while i < 11:
#         producto = numero * i
#         print(numero,' x ',i,' = ',producto)
#         i += 1
# else:
#     print('Introduzca un numero valido')

# Solucion alterna

# tabla = int(input('Introduzca un numero para generar la tabla: '))

# for i in range(1,11):
#     producto = tabla * i
#     print(tabla,i,sep=' x ',end=' = ')
#     print(producto)

# Con tamaño variable de la tabla

tabla = int(input('Introduzca un numero para generar la tabla: '))
tamaño = int(input('Introduzca un numero para el tamaño de la tabla: '))

for i in range(1,tamaño+1):
    producto = tabla * i
    print(tabla,i,sep=' x ',end=' = ')
    print(producto)