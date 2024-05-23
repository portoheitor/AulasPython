#Transforme novamente os arquivos.json em objetos
import json

from ex01_salver_class_json_A import Pessoa

dados1 = 'ex01_salvar_pessoa_dados1.json'
dados2 = 'ex01_salvar_pessoa_dados2.json'
dados3 = 'ex01_salvar_pessoa_dados3.json'


def criar_claas_pessoa(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
        dados = json.load(arquivo)
        nome_pessoa = Pessoa(**dados)
        return nome_pessoa


pessoa1 = criar_claas_pessoa(dados1)
pessoa2 = criar_claas_pessoa(dados2)
pessoa3 = criar_claas_pessoa(dados3)

print(vars(pessoa1))
print(vars(pessoa2))
print(vars(pessoa3))
