'''
Faca um programa que peca ao usuario para digitar um numero inteiro.
informe se esse numero é par ou impar.
caso o usuario nao digite um numero inteiro , informe que nao é um numero inteiro
'''

while True:
    
    num_informado = input('Digite um numero inteiro: ')
    
    if (num_informado.isdigit() == True):
        num_informado = int(num_informado)
        if (num_informado % 2 == 0):
            print(f'O numeror {num_informado} é um numero PAR!')
            break;
        else:
            print(f'O numero {num_informado} é um numeor IMPAR!')
            break;
    else:
        print('Digite um numero INTEIRO! Tente novamente!')