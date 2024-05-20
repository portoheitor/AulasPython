import random

from Conta import Conta


class CriarContaPoupanca(Conta):
    __AGEN_POUPANCA = [500, 599]

    def __init__(self, banco:object):
        super().__init__()
        self.agencia = random.choice(self.__AGEN_POUPANCA)
        self.num_conta = self._NUM_CONTAS__
        self._banco = banco

    def sacar(self, valor: int | float):
        try:
           if self.saldo >= valor:
               self.saldo -= valor
        except Exception as error:
            print(f'Error: {error.__class__.__name__}\n\n{error}\n\n{error.args}')

    def depositar(self, valor: int | float) -> bool:
        self.saldo += valor
        return True

