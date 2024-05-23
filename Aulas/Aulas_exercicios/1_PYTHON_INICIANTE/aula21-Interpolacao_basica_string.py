'''
interpolacao basica de strings

s -> string

d e i -> int

f -> float

x e X -> Hexadecimal
'''

#mesma coisa de C .... prefira FSTRINGS em python fica mais simples e didatico


nome = 'Heitor'
preco = 10000.95897643
variavel = '%s, o preco é R$%.2f' % (nome, preco)

print(variavel)

print('O hexadecimal de %d é %016X' %(1500,1500))
