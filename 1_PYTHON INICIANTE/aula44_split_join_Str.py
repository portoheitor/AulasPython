'''
split e join com list e str

split - Divide uma string (list)
join - une uma string (somente interaveis)
strip - remove os espacos do comeco e final da string
lstrip - remove espacos da esquerda
rstrip - remove espacos da direita
'''

frase = '    Rapadura é doce, mas nao é mole nao!  '
lista_de_frases_cruas = frase.split(', ')

lista_de_frases_fixed = []
for i, frase in enumerate(lista_de_frases_cruas):
    lista_de_frases_fixed.append(lista_de_frases_cruas[i].strip())

# print(lista_de_frases_fixed)
# print(lista_de_frases_cruas)

frases_unidas = ' * '.join(lista_de_frases_fixed)
print(frases_unidas)
