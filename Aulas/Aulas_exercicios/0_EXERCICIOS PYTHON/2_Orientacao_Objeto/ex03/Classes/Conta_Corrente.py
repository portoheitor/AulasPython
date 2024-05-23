import random

from Conta import Conta


class ContaCorrente(Conta):

    __TARIFA_SAQUE_CC_CORRENTE: float = 0.1
    __LIMITE_CHEQUE_ESPECIAL = 100
    __AGENCIA_CONTA_CORRENTE = [534,262,157]

    def __init__(self):
        super().__init__()
        self.agencia = random.choice(self.__AGENCIA_CONTA_CORRENTE)
        self._cheque_especial: int | float = 0.00

    @property
    def cheque_especial(self):
        return self._cheque_especial

    @cheque_especial.setter
    def cheque_especial(self, valor: int | float):
        self._cheque_especial = 0 - valor

    def sacar(self, valor: int | float):
        """
        Metodo de sacar, verifica de qual credito o cliente quer sacar, se saldo conta ou chque especial
        se o limite da conta estiver zerado ele informa que nao tem saldo,
        se o limite de chueque especial ja estiver extourado informa que nao tem mais limite,
        caso contarrio efetua o saca de uma das duas opcoes disponiveis caso aja credito
        """
        try:
            conta = input(f'Escolha a opcao para Sacar:\n'
                          f'- Saque Conta Corrente [1]\n- Saque Limite Cheque Especial [2]')
            if conta == '1':
                if self._saldo >= valor:
                    debitar = (valor + (self.__TARIFA_SAQUE_CC_CORRENTE * valor))
                    self._saldo -= debitar
                else:
                    raise ValueError('Saldo insulficiente!')
            elif conta == '2':
                if self._cheque_especial <= self.__LIMITE_CHEQUE_ESPECIAL:
                    debitar = (valor + (self.__TARIFA_SAQUE_CC_CORRENTE * valor))
                    self._cheque_especial -= debitar
                else:
                    raise ValueError('Sem limite Cheque Especial!')
            else:
                raise ValueError('Digitar apenas as opcoes 1 ou 2')
        except Exception as error:
            print(f'Error: {error.__class__.__name__}\n\n{error}\n\n{error.args}')

    def depositar(self, valor: int | float) -> None:
        """
        Metodo verifica se o valor do cheque especial é negativo, se for atualiza o valor do chuque especial
        Se o valor do deposito for sulficiente para cobrir e sobrar dinheiro a sobra vai para o saldo da conta
        Se o cheque especial estiver zerado o valor integral vai para o saldo da conta
        """
        try:
            if self._cheque_especial <= 0:
                diferenca = 0
                self._cheque_especial += valor
                if self._cheque_especial > 0:
                    diferenca = self._cheque_especial - 0
                    self._cheque_especial -= diferenca
                    self._saldo += diferenca
                elif diferenca > 0:
                    self.saldo += diferenca
            else:
                self.saldo += valor

        except Exception as error:
            raise error.args

    def __repr__(self):
        class_name = type(self).__name__
        attrs = (f'(Agencia: {self._agencia!r}, Saldo:{self._saldo!r}, Cheque_Especial:{self._cheque_especial!r},'
                 f' Numero Conta:{self._num_conta!r})')
        return f'{class_name}{attrs}'

if __name__ == "__main__":
    cc1 = ContaCorrente()
    # cc1.depositar(50)
    cc1.cheque_especial = 50
    print("saldo", cc1.saldo)
    print(f'chque especial {cc1.cheque_especial}')
    print()
    cc1.depositar(100)
    print("saldo", cc1.saldo)
    print(f'chque especial {cc1.cheque_especial}')
    cc1.sacar(10)
    print("saldo", cc1.saldo)
    print(f'chque especial {cc1.cheque_especial}')