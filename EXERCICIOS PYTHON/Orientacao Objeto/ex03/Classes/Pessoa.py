from abc import ABC, abstractmethod


class Pessoa():
    def __init__(self):
        self._nome = None
        self._idade = None

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
            print(f'Parametro deve ser uma String!\n {erro.args}\n{erro.__class__.__name__}')

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
            print(f'Parametro deve ser um INT !\n {erro.args}\n{erro.__class__.__name__}')
