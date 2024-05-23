'''
Repeticoes 
while (enquanto)
Executa uma acao enquanto uma condicao for verdadeeira
'''
condicao = True
while condicao:
    nome = input('Seu nome é: ')
    print(f'{nome}')
    if nome == 'sair':
       condicao = False
