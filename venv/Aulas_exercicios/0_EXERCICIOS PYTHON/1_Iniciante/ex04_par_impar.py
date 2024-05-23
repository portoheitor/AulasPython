'''
Escreva um programa que peça ao usuário para digitar um número e imprima se ele é par ou ímpar.
'''

def is_number(inputs):
    try:
        float(inputs)
        return True
    except:
        return False


while True:
    num1 = input('Digite um numero para verificacao: ')
    verificacao = is_number(num1)
    if verificacao:
        if (float(num1) % 2 == 0):
            print(f'O numero {num1} é um numero PAR!')
            break
        else:
            print(f'O numero {num1} é um numero IMPAR!')
            break;
    else:
        print('Digite apenas Numeros!\nTente novamente....')
    