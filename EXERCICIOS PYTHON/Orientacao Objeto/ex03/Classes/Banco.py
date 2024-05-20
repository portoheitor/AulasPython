from Cliente import Cliente
from Conta_Corrente import CriarContaCorrente
from Conta_Poupanca import CriarContaPoupanca


class Banco:
    def __init__(self, nome_banco: str):
        self._nome_banco = nome_banco
        self._cliente = Cliente
        self._conta_corrente = CriarContaCorrente
        self._conta_poupanca = CriarContaPoupanca

    @property
    def nome(self):
        return self._nome_banco

