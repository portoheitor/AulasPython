'''
CUIDADOS COM DADOS MUTAVEIS

=  -  Copiando o valor (imutaveis)
=  -  Aponta para o mesmo valor na memoria (mutavel)

'''

lista_a = ['Heitor', 'Maite']
lista_b = lista_a.copy()

lista_a[0] = 'Outro valor'

print(lista_a)
print(lista_b)