class Publicacion:
    def __init__(self, nombre, autor, fecha_publicacion, tipo_publicacion):
        self.nombre = nombre
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.tipo_publicacion = tipo_publicacion
    
    def agregar_a_historial(self, historial, publicacion):
        historial.append(publicacion)
        return historial
    
    def imprimir_publicacion(self):
        print(f'''                  Nombre: {self.nombre}
        Autor: {self.autor}
        Fecha de publicacion: {self.fecha_publicacion}
        Tipo de publicacion: {self.tipo_publicacion}''')