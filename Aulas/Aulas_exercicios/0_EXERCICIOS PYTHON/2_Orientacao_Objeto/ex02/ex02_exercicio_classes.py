# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome_modelo):
        self._nome_carro = nome_modelo

    @property
    def nome_modelo(self):
        return self._nome_carro

    @nome_modelo.setter
    def nome_modelo(self, nome):
        self._nome_carro = nome


class Fabricante:
    def __init__(self, nome_fabricante):
        self._nome_fabricante = nome_fabricante

    @property
    def nome_fabricante(self):
        return self._nome_fabricante

    @nome_fabricante.setter
    def nome_fabricante(self, nome):
        self._nome_fabricante = nome


class Motor:
    def __init__(self, nome_motor):
        self._nome_motor = nome_motor

    @property
    def nome_motor(self):
        return self._nome_motor

    @nome_motor.setter
    def nome_motor(self, nome):
        self._nome_motor = nome


"""
CLASSE PARA FABRICAR CARROS
"""





class FabricarCarro:
    def __init__(self, nome_fabricante, nome_modelo, tipo_motor):
        if isinstance(nome_fabricante, str) and isinstance(nome_modelo, str) and isinstance(tipo_motor, str):
            self._fabricante = Fabricante(nome_fabricante)
            self._modelo = Carro(nome_modelo)
            self._motor = Motor(tipo_motor)
        else:
            raise TypeError('Todos os atributos devem ser STR')

    @property
    def caracteristicas(self):
        return f'Fabricante: {self._fabricante.nome_fabricante}\nModelo: {self._modelo.nome_modelo}\nMotor: {self._motor.nome_motor}\n'

    @property
    def modelo(self):
        return self._modelo.nome_modelo

    @modelo.setter
    def modelo(self, nome):
        self._modelo.nome_modelo = nome

    @property
    def motor(self):
        return self._motor.nome_motor

    @motor.setter
    def motor(self, nome):
        self._motor.nome_motor = nome

    @property
    def fabricante(self):
        return self._fabricante.nome_fabricante

    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante.nome_fabricante = nome
