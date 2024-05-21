from abc import ABC, abstractmethod


class Pessoa():
    def __init__(self, nome:str, idade:int, cpf:str):
        self._nome = nome
        self._idade = idade
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome: str):
        try:
            if isinstance(nome, str):
                self._nome = nome
            else:
                raise ValueError
        except ValueError as erro:
            raise erro.args

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, anos: int):
        try:
            if isinstance(anos, int):
                self._idade = anos
            else:
                raise ValueError
        except ValueError as erro:
            raise erro.args

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf:str):
        self._cpf = cpf
