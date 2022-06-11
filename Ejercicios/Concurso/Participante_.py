class Participante:
    def __init__(self, nombre, formato, categoria, telefono, registro):
        self.nombre = nombre
        self.formato = formato
        self.categoria = categoria
        self.telefono = telefono
        self.registro = registro
    
    def imprimir_concursante(self):
        print(f'''      *** PARTICIPANTE ***
        Nombre: {self.nombre}
        Formato: {self.formato}
        Categoria: {self.categoria}
        Telefono: {self.telefono}
        Numero de registro: {self.registro}''')
    
