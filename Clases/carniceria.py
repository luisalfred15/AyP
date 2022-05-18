print('Bienvenido a la carniceria')

cedula = input('Ingrese su cedula')
nombre = input('Ingrese su nombre')
corte_carne = input('Ingrese el corte de carne deseado que vale, por kilo: \n 1: Lomito, 15$ \n 2: Punta, 8$ \n Molida, 6$ \n')
kilos = int(input('Ingrese los kilos a comprar:'))
precio_final = 0

 = {
    1: {
        'name': 'Lomito',
        'price': 15
    },
    2: {
        'name': 'Punta',
        'price': 8
    },
    3: {
        'name': 'Molida',
        'price': 6
    }
}

def calculo_factura(opcion_corte):
    if corte_carne == opcion_corte:
        precio_corte = 15
        precio_final = kilos * precio_corte

def imprimir_factura():
    print(''' FACTURA
    ''')