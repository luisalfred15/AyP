class Alumno:
    def __init__(self, nombre, grado, promedio, direccion, nombre_representante, telefono_representante):
        self.nombre = nombre
        self.grado = grado
        self.promedio = promedio
        self.__direccion = direccion
        self.nombre_representante = nombre_representante
        self.__telefono_representante = telefono_representante
        self.becado = False
    
    def obtenerDireccion(self):
        return self.__direccion
    
    def obtenerTelefono(self):
        return self.__telefono_representante
    
    def esBecado(self, promedio):
        if int(promedio) >= 18:
            return 'Si'
        else:
            return 'No'

# Se pudo haber agregado aqui la funcion para imprimir la informacion del alumno