'''
receba 2 valores do usuario
faca um programa que identifica qual é o maior valor e 
printa na tela qual maior valor
'''

def is_number(inputs):
    try:
        float(inputs)
        return True
    except ValueError:
        return False
       
        
num1 = input('Digite um numero para comparar: ')
num2 = input('Digite um outro numero para comparar: ')

while True:
    if is_number(num1) and is_number(num2):
        if int(num1) > int(num2):
            print(f'{int(num1)} é Maior que {int(num2)}')
            break
        elif int(num1) < int(num2):
            print(f'{int(num2)} é Maior que {int(num1)}')
            break
        elif int(num1) == int(num2):
            print(f'Os numeros {int(num1)} e {int(num2)} sao Iguais!')
            break
        else:
            print('Erro de sintaxe!')
            break
    else:
        print('Favor digitar somente NUMEROS! Tente novamente...')
        break