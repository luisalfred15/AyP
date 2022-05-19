def main():
    cesta = {}
    print('Bienvenido!')
    while True:
        opcion = input('Seleccione una opcion: \n 1: Agregar un producto a la cesta \n 2: Finalizar compra \n ->')
        if opcion.isnumeric() and int(opcion) == 1:
            agregar_producto(cesta)
        elif opcion.isnumeric() and int(opcion) == 2:
            imprimir_factura(cesta)
            break
        else:
            print('Por favor, ingrese una opcion valida')

def agregar_producto(cesta):
    producto = input('Por favor, escriba el producto deseado: ')
    precio = input('Por favor escribe el precio del producto: ')
    while precio.isalpha() or int(precio) < 0:
        precio = input('Por favor, ingrese un precio valido: ')
    cesta[producto] = float(precio)

def imprimir_factura(cesta):
    total = 0
    print('Lista de la compra')
    for productos, precios in cesta.items():
        total += precios
        print(f'{productos.capitalize()}: Bs. {precios}')
    print(f'Total: Bs. {total}')

main()