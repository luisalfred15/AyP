from Empleado_ import Empleado

class Redactor(Empleado):
    def __init__(self, nombre, cedula, seccion):
        super().__init__(nombre, cedula, seccion)
    
    def escribir_articulo():
        print('Articulo escrito')
    
    def imprimir_redactor(self, redactor):
        print(f'Nombre: {redactor.get_nombre()} \n Cedula: {redactor.get_cedula()} \n Seccion: {redactor.get_seccion()}')