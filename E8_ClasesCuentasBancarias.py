class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo


cuenta = CuentaBancaria("Guillermo Alcaraz", 15.500)
print(f"Titular de la cuenta: {cuenta.titular}")
print(f"Saldo de la cuenta: ${cuenta.saldo}")