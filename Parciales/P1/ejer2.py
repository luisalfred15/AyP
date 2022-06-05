productos = {'Q': 1000, 'F': 2500, 'B': 4000}                                       # Pico mas alto: Pico Bolivar
nombres_productos = {'Q': 'Quimico', 'F': 'Farmaceutico', 'B': 'Biologicos'}        # Año en que se sembro el samanÑ 1972

def main():
    clientes = {}
    contador_clientes = 1
    opcion = 'S'
    print('Bienvenido a Saman Laboratorios!')
    while True:
        if opcion.upper() == 'S':    
            rif = int(input('Por favor, introduzca su RIF: '))
            linea_producto = input('''Por favor, introduzca la linea de producto que esta comprando: 
                                        Q: Quimico
                                        F: Farmaceutico
                                        B: Biologico
                                        -> ''')
            forma_pago = input('''Por favor, introduzca la linea de producto que esta comprando: 
                                        C: Contado
                                        R: Credito
                                        -> ''')
            
            costo = calcular_costo(linea_producto)
            descuento = int(calcular_descuento(rif_primo, forma_pago, costo))
            impuesto = int(calcular_impuesto(linea_producto, costo))
            total = calcular_total(costo, impuesto, descuento)
            recargo(forma_pago, total)

            clientes[contador_clientes] = {
                'rif': rif,
                'linea_producto': linea_producto,
                'forma_pago': forma_pago,
                'descuento': descuento,
                'impuesto': impuesto,
                'total': total + recargo(forma_pago, total)
            }

            contador_clientes += 1

            opcion = input('''Desea agregar otro cliente?
                            S: Si
                            N: No
                            -> ''')
        imprimir_informe(clientes, linea_producto)
        break

def calcular_costo(linea_producto):
    return productos.get(linea_producto)

def calcular_descuento(rif_primo, forma_pago, costo):
    descuento = 0
    if forma_pago == 'C':
        descuento += 0.03 * costo
    if costo % 2 == 0:
        descuento += 0.02 * costo
    if rif_primo:
        descuento += 0.05 * costo
    return descuento

def rif_primo(rif):
    aux = 0
    for i in range(1, rif + 1):
        if rif % i == 0:
            aux += 1
    if aux > 2:
        rif_primo = False
    return rif_primo

def calcular_impuesto(linea_producto, costo):
    impuesto = 0
    if linea_producto == 'Q' or linea_producto == 'B':
        impuesto += 0.12 * costo
    return impuesto

def calcular_total(costo, impuesto, descuento):
    total = 0
    total = costo + impuesto - descuento
    return total

def recargo(forma_pago, total):
    recargo = 0
    if forma_pago == 'R':
        recargo += 0.1 * total
    return recargo

def imprimir_informe(clientes, linea_producto):
    print('*** INFORME ***')
    for key, value in clientes.items():
        print(f'''          RIF: {value.get('rif')}
        Linea de producto adquirida: {nombres_productos.get(linea_producto)}
        Codigo de la forma de pago: {value.get('forma_pago')}
        Monto del descuento: {value.get('descuento')}
        Monto del impuesto: {value.get('impuesto')}
        Total a pagar: {value.get('total')}''')

main()