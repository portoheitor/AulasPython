import random

from Conta import Conta


class CriarContaCorrente(Conta):
    _TARIFA_SAQUE_CC_CORRENTE: float = 0.12
    _LIMITE_CHEQUE_ESPECIAL = 100

    def __init__(self) -> None:
        super().__init__()
        self.agencia = random.choice([555, 157, 332])
        self.num_conta = random.randint(1, 10000)
        self._cheque_especial = 0
        self._cliente = None

    def sacar(self, valor: int | float) -> bool:
        try:
            if self.saldo >= valor:
                self.saldo -= valor
            else:
                raise ValueError('Saldo insulficiente!')
        except Exception as error:
            print(f'Error: {error.__class__.__name__}\n\n{error}\n\n{error.args}')

    def debitar_cheque_especial(self) -> int | float:
        try:
            saldo = self.saldo
            cheque_especial = self._cheque_especial
            if saldo >= cheque_especial:
                valor_debitar = cheque_especial
                return valor_debitar
            else:
                valor_debitar = saldo
                return valor_debitar
        except Exception as error:
            print(f'Error: {error.__class__.__name__}\n\n{error}\n\n{error.args}')

    def depositar(self, valor: int | float) -> None:
        try:
            self.saldo = valor
        except Exception as error:
            print(f'Error: {error.__class__.__name__}\n\n{error}\n\n{error.args}')


c1 = CriarContaCorrente()
c1.depositar(30)
print(c1.saldo, c1.num_conta, c1.agencia)

c1.sacar(40)
print(c1.saldo, c1.num_conta, c1.agencia)

#
# c2 = CriarContaCorrente()
# print(c2.saldo, c2.num_conta, c2.agencia)
