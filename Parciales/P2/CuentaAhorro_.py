from Cuenta_ import Cuenta

class CuentaAhorro(Cuenta):
    def __init__(self, num_cuenta, saldo, interes):
        super().__init__(num_cuenta, saldo)
        self.tipo_cuenta = 'Ahorro'
        self.interes = interes