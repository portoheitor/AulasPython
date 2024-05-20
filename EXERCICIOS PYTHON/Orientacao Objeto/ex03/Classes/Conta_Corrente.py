import random

from Conta import Conta


class CriarContaCorrente(Conta):
    """
    Class criar conta corrente do cliente
    Conta corrente tem um limite pre estabelecido de R$100,00 de cheque especial
    Saques na conta corrente tem tarifa padrao adicionada ao efetuar saques.
    """
    __TARIFA_SAQUE_CC_CORRENTE: float = 0.12
    __LIMITE_CHEQUE_ESPECIAL = 100
    __AGEN_CC_CORRENTE = [555, 157, 332]

    def __init__(self, banco:object) -> None:
        super().__init__()
        self.agencia = random.choice(self.__AGEN_CC_CORRENTE)
        self.num_conta = self._NUM_CONTAS__
        self._cheque_especial = 0
        self._banco = banco


    @property
    def cheque_especial(self):
        return self._cheque_especial

    @cheque_especial.setter
    def cheque_especial(self, valor):
        self._cheque_especial = valor

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
                if self.saldo >= valor:
                    debitar = (valor * self.__TARIFA_SAQUE_CC_CORRENTE)
                    self.saldo -= debitar
                else:
                    raise ValueError('Saldo insulficiente!')
            elif conta == '2':
                if self._cheque_especial <= self.__LIMITE_CHEQUE_ESPECIAL:
                    debitar = (valor * self.__TARIFA_SAQUE_CC_CORRENTE)
                    self._cheque_especial -= debitar
                else:
                    raise ValueError('Sem limite Cheque Especial!')
            else:
                raise ValueError('Digitar apenas as opcoes 1 ou 2')
        except Exception as error:
            print(f'Error: {error.__class__.__name__}\n\n{error}\n\n{error.args}')

    def deposita(self, valor: int | float) -> None:
        """
        Metodo verifica se o valor do cheque especial é negativo, se for atualiza o valor do chuque especial
        Se o valor do deposito for sulficiente para cobrir e sobrar dinheiro a sobra vai para o saldo da conta
        Se o cheque especial estiver zerado o valor integral vai para o saldo da conta
        """
        try:
            if self._cheque_especial < 0:
                diferenca = 0
                self._cheque_especial += valor
                if self._cheque_especial >= 0:
                    diferenca = self._cheque_especial - 0
                    self._cheque_especial -= diferenca
                    self.saldo += diferenca
                else:
                    return self.deposita(diferenca)
            else:
                self.saldo += valor

        except Exception as error:
            print(f'Error: {error.__class__.__name__}\n\n{error}\n\n{error.args}')

