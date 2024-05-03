'''
Exercicio: Exiba os indices da lista

0 Heitor
1 Maite
2 Arielle

'''

lista = ['Heitor', 'Maite', 'Arielle', 'Jose', 'Lourdes']
lista.append('Bradock')

indices_lista = range(len(lista))
for index in indices_lista:
    print(index, lista[index], type(lista[index]))
