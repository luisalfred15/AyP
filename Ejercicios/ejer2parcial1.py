precios_productos = {'Q': 1000, 'F': 2500, 'B': 4000}
nombres_productos = {'Q': 'Quimico', 'F': 'Farmaceutico', 'B': 'Biologicos'}

def main():
    print('Bienvenido a Saman Internacional!')
    while True:
        rif = input('Ingrese su RIF: ')
        while not(rif.isnumeric() and int(rif) >= 0):
            rif = input('Por favor, ingrese un RIF valido: ')
        producto = input('''Ingrese el producto que desea comprar: 
                                Q: Quimico
                                F: Farmaceutico
                                B: Biologicos
                                -> ''')
        producto = producto.capitalize()
        while not(producto == 'Q' or producto == 'F' or producto == 'B'):
            producto = input('Por favor, elija un producto de entre las opciones: ')
            producto = producto.capitalize()
        forma_pago = input('''Ingrese la forma de pago que va a emplear:
                                C: Contado
                                R: Credito
                                -> ''')
        forma_pago = forma_pago.capitalize()
        while not(forma_pago == 'C' or forma_pago == 'R'):
            forma_pago = input('Por favor, elija un metodo de pago de entre las opciones: ')
            forma_pago = forma_pago.capitalize()
        
        monto = precios_productos.get(producto)
        
        rif_es_primo(int(rif))
        rif_es_par(int(rif))
        descuento = calcular_descuento(forma_pago, rif_es_par, rif_es_primo, monto)
        impuesto = calcular_impuesto(producto, monto, descuento)
        recargo = calcular_recargo(monto, descuento, forma_pago)
        total = calcular_total(monto, descuento, impuesto, recargo)
        imprimir_informe(rif, producto, forma_pago, descuento, impuesto, total)





def calcular_descuento(forma_pago, rif_es_par, rif_es_primo, monto):
    descuento = 0
    if forma_pago == 'C':
        descuento += 0.03
    if rif_es_par:
        descuento += 0.02
    if rif_es_primo:
        descuento += 0.05
    descuento = monto * descuento
    return descuento

def rif_es_par(rif):
    rif_es_par = False
    if rif % 2 == 0:
        rif_es_par = True
    return rif_es_par

def rif_es_primo(rif):
    rif_es_primo = False
    for i in range(1, rif + 1):
        if rif % i == 0:
            rif_es_primo = True
    return rif_es_primo

def calcular_impuesto(producto, monto, descuento):
    if producto == 'Q' or producto == 'B':
        impuesto = (monto - descuento) * 0.12
    else:
        impuesto = 0    
    return impuesto

def calcular_recargo(monto, descuento, forma_pago):
    if forma_pago == 'R':
        recargo = (monto - descuento) * 0.1
    else:
        recargo = 0    
    return recargo

def calcular_total(monto, descuento, impuesto, recargo):
    total = monto - descuento + impuesto + recargo
    return total

def imprimir_informe(rif, producto, forma_pago, descuento, impuesto, total):
    print(f'''                              *** INFORME ***
                                RIF del comprador: {rif}
                                Producto comprado: {nombres_productos.get(producto)}
                                Forma de pago: {forma_pago}
                                Monto del descuento: {descuento}
                                Monto del impuesto: {impuesto}
                                Total a pagar: {total}''')

main()