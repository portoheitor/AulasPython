'''
Crie as variaveis : nome, sobrenome,
                    idade, ano nascimento,
                    maior de idade,
                    altura metros
                    
imprima na tela
'''
import datetime

nome = 'Heitor'
sobrenome = 'Porto'
idade = 30
data_nascimento = datetime.datetime(1993, 12, 29)
ano_nascimento = data_nascimento.year
maior_de_idade = idade >= 18
altura_metros = 1.76

print(f'Nome: {nome}\nSobrenome: {sobrenome}\nIdade: {idade}\nAltura: {altura_metros}\nMaior de Idade: {maior_de_idade}')
