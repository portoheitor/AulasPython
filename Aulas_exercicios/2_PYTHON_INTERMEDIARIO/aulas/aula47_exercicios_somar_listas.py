'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
'''
from itertools import zip_longest

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

def soma_lista(lista1, lista2):
    indices_listas = min(len(lista1), len(lista2))
    return [(lista1[i] + lista2[i])
            for i in range(indices_listas)]

print(f'Usando funcao \n{soma_lista(lista_a, lista_b)}')

print()

lista_somadas = [x + y for x, y in zip(lista_a, lista_b)]
print((f'Usando List compreention + zip ->  \n{lista_somadas}'))


print()

lista_somadas_longest = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue = 0)]
print(f'Usando List Compreention + zip_longest -> \n {lista_somadas_longest}')