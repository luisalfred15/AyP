class Empleado:
    def __init__(self, nombre, cedula, seccion):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__seccion = seccion
    
    def get_nombre(self):
        return self.__nombre
    
    def get_cedula(self):
        return self.__cedula
    
    def get_seccion(self):
        return self.__seccion