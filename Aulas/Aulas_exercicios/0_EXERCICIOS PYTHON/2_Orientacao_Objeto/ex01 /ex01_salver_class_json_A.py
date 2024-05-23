# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json


class Pessoa:

    def __init__(self, nome, idade, profissao, endereco):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        self.endereco = endereco

    def salvar_json(self, caminho):
        with open(caminho, 'w', encoding='utf8') as arquivo:
            json.dump(self.__dict__, arquivo, indent=2, ensure_ascii=False)
        return


pessoa1 = Pessoa('Heitor Porto', 30, 'Developer', 'Padre Carbone')
pessoa2 = Pessoa('Maite Porto', 1, 'Bagunceira', 'Padre Carbone')
pessoa3 = Pessoa('Arielle Freitas', 27, 'Analista Fiscal', 'Padre Carbone')

pessoa1.salvar_json('ex01_salvar_pessoa_dados1.json')
pessoa2.salvar_json('ex01_salvar_pessoa_dados2.json')
pessoa3.salvar_json('ex01_salvar_pessoa_dados3.json')
