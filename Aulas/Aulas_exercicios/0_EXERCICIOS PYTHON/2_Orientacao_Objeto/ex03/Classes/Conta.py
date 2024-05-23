""" Implementaçao classe conta

Classe conta sera uma classe abstrata
Tera o methodo sacar para ser sobreescrito
"""

from abc import ABC, abstractmethod


class Conta(ABC):
    _CONTAS_CRIADAS = 0

    def __init__(self):
        Conta._CONTAS_CRIADAS += 1
        self._agencia = None
        self._num_conta = self._CONTAS_CRIADAS
        self._saldo = 0.00

    @abstractmethod
    def sacar(self, valor: int | float) -> bool:
        ...
    @abstractmethod
    def depositar(self, valor: int | float) -> None:
        ...

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor: int | float):
        try:
            self._saldo += valor
        except Exception as error:
            raise error.args

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, numero: int):
        try:
            self._agencia = numero
        except Exception as error:
            raise error.args

    @property
    def num_conta(self):
        return self._num_conta

    @num_conta.setter
    def num_conta(self, numero: str | int):
        try:
            self._num_conta = numero
        except Exception as error:
            raise error.args
