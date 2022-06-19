from funciones import *

parking_lot = [
{
"type": "AUTOMOVIL",
"plate": "ABC12D",
"brand": "Chevrolet",
"spot": "A12",
"arrival": "10:00:36",
"handicapped": False
},
{
"type": "MOTOCICLETA",
"plate": "EFG34H",
"brand": "Suzuki",
"spot": "B10",
"arrival": "10:20:15"
},
{
"type": "AUTOMOVIL",
"plate": "IJK56M",
"brand": "Mazda",
"spot": "A33",
"arrival": "11:48:22",
"handicapped": False
}
]

def main():
    print('Bienvenido al Parking de la Unimet!')
    while True:
        opcion = comprobar_opcion('''Seleccione la opcion deseada:
        1. Registrar un vehiculo
        2. Ver los vehiculos registrados
        3. Registrar la salida de un vehiculo
        -> ''')








main()