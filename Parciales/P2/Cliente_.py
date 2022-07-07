class Cliente:
    def __init__(self, nombre, cedula, estado_civil, cuenta):
        self.nombre = nombre
        self.cedula = cedula
        self.estado_civil = estado_civil
        self.cuenta = cuenta
    
    def imprimir_cliente(self):
        print(f'''Nombre: {self.nombre}
        Cedula: {self.cedula}
        Estado civil: {self.estado_civil}
        Saldo en la cuenta: {self.cuenta.saldo}''')