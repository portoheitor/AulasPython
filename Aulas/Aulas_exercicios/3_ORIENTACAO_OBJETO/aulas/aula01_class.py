# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.
# string = 'Heitor'  # str
# print(string.upper())
# print(isinstance(string, str))
class Pessoa:
    def __init__(self,nome:str, sobrenome:str, idade:int):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade


p1 = Pessoa('Heitor', 'Porto', 30)
p2 = Pessoa('Arielle','Freitas', idade=27)

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)