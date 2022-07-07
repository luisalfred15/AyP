from Cuenta_ import Cuenta

class CuentaCorriente(Cuenta):
    def __init__(self, num_cuenta, saldo, chequeras):
        super().__init__(num_cuenta, saldo)
        self.tipo_cuenta = 'Corriente'
        self.chequeras = chequeras
    
    def retiro(self, monto):
        self.saldo += monto + monto * 0.1
        return 