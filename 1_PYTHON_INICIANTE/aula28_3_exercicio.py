'''
Faca um programa que peca o primeiro nopme do usuario
Se o nome tiver 4 letras ou menos
    escreva Seu nome e curtoi
Se o nome tiver 5 a 6 letras
    escrevva seu nome é normal
Se o nome tiver mais que 6 letras
    escreva seu nome é muito grande
'''

while True:
    nome = input('Digite seu primeiro nome: ')
    if nome.isdigit():
        print('Nome so pode conter LETRAS')
    else:
        contagem_letras = len(nome)
        if (contagem_letras > 0 and contagem_letras <= 4):
            print(f'Seu nome {nome} é CURTO')
            break
        elif (contagem_letras > 4 and contagem_letras <= 6):
            print(f'Seu nome {nome} é NORMAL')
            break
        else:
            print(f'Seu nome {nome} é MUITO GRANDE!')
            break