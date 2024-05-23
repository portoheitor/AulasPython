import random

from Conta import Conta


class ContaPoupanca(Conta):
    __AGENCIA_CONTA_POUPANCA = [663, 500]

    def __init__(self):
        super().__init__()
        self.agencia = random.choice(self.__AGENCIA_CONTA_POUPANCA)

    def sacar(self, valor: int | float) -> bool:
        try:
            if self._saldo < valor:
                raise ValueError(f'Saldo Insulficiente {self.saldo}')
            else:
                self._saldo -= valor
                return True
        except Exception as error:
            raise error.args

    def depositar(self, valor: int | float) -> None:
        try:
            if valor > 0:
                self.saldo += valor
            else:
                raise ValueError(f'Valor menor que Zero! {valor}')
        except Exception as error:
            raise error.args

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'(Agencia: {self._agencia!r}, Saldo:{self._saldo!r},Numero Conta:{self._num_conta!r})'
        return f'{class_name}{attrs}'


if __name__ == "__main__":
    pp1 = ContaPoupanca()
    print(pp1.saldo, pp1.agencia, pp1.num_conta)
    pp1.depositar(30)
    print(pp1.saldo, pp1.agencia, pp1.num_conta)
    pp1.sacar(20)
    print(pp1.saldo, pp1.agencia, pp1.num_conta)

