""" Implementaçao classe conta

Classe conta sera uma classe abstrata
Tera o methodo sacar para ser sobreescrito
"""

from abc import ABC, abstractmethod
import random


class Conta(ABC):

    def __init__(self):
        self._agencia = False
        self._num_conta = False
        self._saldo = 0.00

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor: int | float):
        self._saldo = valor

    @property
    def agencia(self):
        return self._agencia

    @agencia.setter
    def agencia(self, numero: int):
        try:
            if self._agencia is False:
                self._agencia = numero
            else:
                raise AttributeError('Numero de Agencia ja atribuido')
        except Exception as error:
            print(f'Error: {error.__class__.__name__}\n\n{error}\n\n{error.args}')

    @property
    def num_conta(self):
        return self._num_conta

    @num_conta.setter
    def num_conta(self, numero: str | int):
        try:
            if self._num_conta is False:
                self._num_conta = numero
            else:
                raise AttributeError('Numero de Conta ja atribuido')
        except Exception as error:
            print(f'Error: {error.__class__.__name__}\n\n{error}\n\n{error.args}')

    @abstractmethod
    def sacar(self, valor: int | float) -> bool:
        ...
