# Atributos de Classs

class Pessoa:
    ano_atual = 2022  # atributo da classe , disponivel em todas as instancias

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


pessoa1 = Pessoa('Heitor', 30)
pessoa2 = Pessoa('Helena', 12)

print(pessoa1.get_ano_nascimento())
print(pessoa2.get_ano_nascimento())