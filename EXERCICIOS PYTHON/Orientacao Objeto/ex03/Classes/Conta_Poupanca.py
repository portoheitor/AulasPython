import Conta
import random


class CriarContaPoupanca(Conta):
    AGEN_CC_POPANCA = random.choice([500, 599])

    def __init__(self):
        super().__init__()
        super()._agencia = self.AGEN_CC_POPANCA

    def sacar(self, valor: int | float) -> bool:
        try:
            if valor <= self._saldo:
                self._saldo -= valor
                return True
            else:
                return False
        except Exception as error:
            print(f'Error: {error.__class__.__name__}\n\n{error}\n\n{error.args}')

    def depositar(self, valor: int | float) -> bool:
        super()._saldo += valor
        return True
