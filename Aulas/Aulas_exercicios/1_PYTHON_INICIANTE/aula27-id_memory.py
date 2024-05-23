'''
Flag =  MArcar um local

None = nao valor

is e is not = é ou nao é (tipo, valor, identidade)

id = identidade

'''

valor1 = 'a'
valor_2 = 'a'
valor_3 = 'A'
print(id(valor1))
print(id(valor1))
print(id(valor_3))

condicao =  True
passou_no_if = None
if condicao:
    passou_no_if = True
    print('Faca algo')
else:
    print('Nao faca algo')
    
if passou_no_if is None:
    print('Nao Passou no IF')
else:
    print('Passou no IF')

