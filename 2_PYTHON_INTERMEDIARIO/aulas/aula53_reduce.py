# reduce -> faz a reducao de um iteravel em um unico valor
#  ex: qual a quantidade de produtos///
#   qual valor total dos produtos
# reduce(funcao , iteravel , 0) sempre colocar o parametro inicial para nao haver erros
# ela passa automaticamente o acumulador como o valor do parametro inicial

from functools import reduce

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

valor_total = reduce(
    lambda acumulador, produto: produto['preco'] + acumulador,
    produtos,
    0
)

print(f'Valor total = {valor_total}')
