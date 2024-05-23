'''
Formatacao basica de Strings (fStrings)

s -> String
d -> Int
f -> float
.<num>f -> casas decimais
x ou X -> Hexadecimal
(Caractere)(><^)(quantidade)

> -> esquerda
< -> direita
^ -> centro

Sinal -+ ou -  EX: 0>-100,.1f

Conversion Flags - !r -> !s ->  !a
'''

#prefira usar bibliotecas para formatar Dinheiro.. valores ... enfim
# tudo que envolva matematica use BIBLIOTECAS


varialvel = 'ABC'

print(f'{varialvel: >10}')
print(f'{1000092394:+,.2f}')
print(f'O hexadecimal de 1500 é: {1500:08X}')