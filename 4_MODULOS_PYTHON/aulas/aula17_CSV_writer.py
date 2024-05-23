import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula17_CSV.csv'

lista_clientes = [
    {'Nome': 'Heitor Porto', 'Idade': '30', 'Endereco': 'Av Brasil, 21, Centro'},
    {'Nome': 'João da Silva', 'Idade': '55', 'Endereco': 'Rua 22, 44, Nova Era'},
    {'Nome': 'Maite Porto', 'Idade': '1', 'Endereco': 'Rua Padre Carbone'},
]

"""
Escrevendo csv com Dict

"""
with open(CAMINHO_CSV, 'w') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.DictWriter(
        arquivo,
        fieldnames=nome_colunas
    )
    escritor.writeheader()

    for cliente in lista_clientes:
        print(cliente)
        escritor.writerow(cliente)



"""
ESCREVENDO COM LISTA , ESCREVE LINHA POR LINHA

with open(CAMINHO_CSV, 'w', encoding='utf-8') as arquivo:
    nome_colunas = lista_clientes[0].keys()
    escritor = csv.writer(arquivo)

    escritor.writerow(nome_colunas)


    for cliente in lista_clientes:
       escritor.writerow(cliente.values())
"""