'''
defina o nome, altura, peso
calcule o IMC

O Índice de Massa Corporal (IMC) 
é calculado dividindo o peso (em quilogramas) 
pela altura ao quadrado (em metros).
'''

nome = 'Heitor'
altura = 1.76
peso = 85.5
imc = peso / altura ** 2

print(f'{nome}, voce tem {altura}cm\nEsta pesando {peso}Kg\nSeu IMC é de: {imc}')