def main():
    estudios = {'U': 
        {
            'name':'Ultrasonido',
            'price': 8900
        },
        'T': {
            'name':'Tomografia',
            'price': 12640
        },
        'R': {
            'name':'Resonancia',
            'price': 15600
        }
    }
    
    numero_paciente = 0
    
    print('Bienvenido a Radiologia!')

    while True:
        cedula = input('Por favor, introduzca su cedula: ')
        edad = input('Por favor, introduzca su edad: ')
        while not(edad.isnumeric()):
            edad = input('Introduzca una edad valida: ')
        sexo = input('Por favor, indique su sexo: \n F: Femenino \n M: Masculino \n ->')
        prueba = input('Por favor, indique la prueba que se desea realizar: \n U: Ultrasonido \n T: Tomografia \n R: Resonancia \n ->')
        costo = estudios[prueba]['price']
        numero_paciente += 1

        es_tercera_edad(edad, sexo)
        descuento = calcular_descuento(es_tercera_edad, numero_paciente, costo)
        total = costo - descuento
        imprimir_factura(cedula, edad, sexo, prueba, total)
    
def es_tercera_edad(edad, sexo):
    if (sexo == 'F' and int(edad) > 55) or (sexo == 'M' and int(edad) > 65):
        return es_tercera_edad == True

def calcular_descuento(es_tercera_edad, numero_paciente, costo):
    descuento = 0
    if es_tercera_edad:
        descuento += costo * 0.25
    if numero_paciente % 2 != 0:
        descuento += costo * 0.02
    return descuento


def imprimir_factura(cedula, edad, sexo, prueba, total):
    print('*** FACTURA ***')
    print('Cedula del paciente: ',cedula)
    print('Edad del paciente: ',edad)
    print('Sexo del paciente: ',sexo)
    print('Prueba realizada: ',prueba)
    print('Total a pagar: ',total)

main()