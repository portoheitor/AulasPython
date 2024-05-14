# Exercício - Unir listas
# Crie uma função zipper
# O trabalho dessa função será unir duas listas na ordem.


# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

from itertools import zip_longest

def zipper(lista1, lista2):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [(lista1[i], lista2[i]) for i in range(intervalo_maximo)]

lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
listas_estados = ['BA', 'SP', 'MG', 'RJ']

print(zipper(lista_cidades,listas_estados))
print()
# ou simplismente usar funcao zip

print('Usando Funcao zip (funcao zip retorna um interator) *usa lista de menor intervalor')
print(list(zip(lista_cidades,listas_estados)))

print()
print('usando funcao zip_longest , *usa a lista de maior intervalor')
print(list(zip_longest(lista_cidades, listas_estados, fillvalue='SEM CIDADE')))
