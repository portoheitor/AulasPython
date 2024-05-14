class Pessoa:
    ano_atual = 2022  # atributo da classe , disponivel em todas as instancias

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade


pessoa = Pessoa('Heitor', 30)

print(pessoa.__dict__)
print(vars(pessoa))

dados = {'nome': 'Heitor', 'idade': 30}

pessoa_duplicada = Pessoa(**dados)

print(vars(pessoa_duplicada))