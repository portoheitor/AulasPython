# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Heitor Ribeiro',
#     'sobrenome': 'Porto',
#     'idade': 30,
#     'altura': 1.76,
#     'endereços': [
#         {'rua': 'Maria Eulalia', 'número': 123},
#         {'rua': 'Padre Carbone', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Heitor Ribeiro', sobrenome='Porto')
pessoa = {
    'nome': 'Heitor Ribeiro',
    'sobrenome': 'Porto',
    'idade': 30,
    'altura': 1.76,
    'endereços': [
        {'rua': 'Maria Eulalia', 'número': 123},
        {'rua': 'Padre Carbone', 'número': 321},
    ],
}
print(pessoa, type(pessoa))
print(pessoa['nome'])
print(pessoa['sobrenome'])

print()

for chave in pessoa:
    print(chave, pessoa[chave])

print()

print(pessoa['endereços'][1])
