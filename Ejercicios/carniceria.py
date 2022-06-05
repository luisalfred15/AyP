precios_carnes = {
    'L': 15,
    'P': 8,
    'M': 6
}

nombres_carnes = {'L': 'Lomito', 'P': 'Punta', 'M': 'Molida'}

def main():
    cerrar_dia = 'N'
    comprar_carne = 'S'
    facturas = {}
    contador_clientes = 1
    print('Bienvenido a Saman Carnes!')
    while cerrar_dia == 'N':
        compra = {}
        total_carne = {}
        nombre = input('Por favor, ingrese su nombre: ')
        cedula = input('Por favor, ingrese su cedula: ')
        contador_carnes = 0
        while comprar_carne == 'S':
            tipo_carne = input('''Por favor, seleccione la opcion de carne:
                                L: Lomito
                                P: Punta
                                M: Molida
                                -> ''')
            kg_carne = input('Por favor, introduzca los kilos que desea de la carne seleccionada anteriormente: ')
            contador_carnes += 1
            compra[contador_carnes] = {
                'kg_carne': kg_carne,
                'tipo_carne': tipo_carne
            }
            comprar_carne = input('''Desea comprar mas carne?
                                        S: Si
                                        N: No
                                        -> ''')

        facturas[contador_clientes] = {
            'nombre': nombre,
            'cedula': cedula,
            'compra': compra
        }
        contador_clientes += 1
        costo = calcular_costo(compra)
        descuento = calcular_descuento(costo, es_primo, es_cuadrado)
        total = calcular_total(descuento, costo)
        imprimir_factura(nombre, cedula, compra, total)
    
        cerrar_dia = input('''Desea finalizar el dia?
                                            S: Si
                                            N: No
                                            -> ''')
        
    
def calcular_costo(compra):
    costo = 0
    for key, value in compra.items():
        costo += int(value.get('kg_carne')) * int(precios_carnes.get(compra[key]['tipo_carne']))
    return costo

def es_primo(costo):
    es_primo = False
    aux = 0                             
    for i in range(1,costo + 1):
        if costo % i == 0:
            aux += 1                
    if aux == 2:                      
        es_primo = True
    return es_primo

def es_cuadrado(costo):
    es_cuadrado = False
    for j in range(1, costo + 1):
        if costo == j ** 2:
            es_cuadrado = True
    return es_cuadrado

def calcular_descuento(costo, es_primo, es_cuadrado):
    descuento = 0
    if costo > 30:
        descuento += 0.05 * costo
    if es_primo:
        descuento += 0.15 * costo
    if es_cuadrado:
        descuento += 0.2 * costo
    return descuento

def calcular_total(descuento, costo):
    total = costo - descuento
    return total

def imprimir_factura(nombre, cedula, compra, total):
    print('             *** FACTURA ***')
    print(f'''              Nombre del cliente: {nombre}
                Cedula del cliente: {cedula}
                Productos:''')
    for key_2, value_2 in compra.items():
        print(f'''              {nombres_carnes.get(value_2.get('tipo_carne'))} ------- {value_2.get('kg_carne')} kg, ${precios_carnes.get(compra[key_2]['tipo_carne']) * int(value_2.get('kg_carne'))}''')
    print(f'                Total: {total}')

def imprimir_fin_dia(contador_clientes, total_carnes):
    print(f'''Cantidad total de clientes: {contador_clientes}
                Kilos vendidos por tipo de carne:''')
    for key_3, value_3 in facturas.items():
        print(f'''{facturas[key_3][compra]}''')

main()