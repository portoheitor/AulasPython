'''
Operadores Logicos

and (e) or (ou) not (nao)

and - Todas as condicoes precisao ser verdadeiras

or -Uma das condicoes tem que ser verdadeira

not - Inverte o valor booleano de uma expressao ( se True vira False, se False vira True)

Existem em python existe o None representa ausencia de valor
É frequentemente usado para indicar que uma variável ou uma função não retornou nenhum valor válido.

'''

# exmeplo dado em aula ficou muito confuso... fiz sistema sem precisar de nenhuma verificacao de curto circuito
#porem fica  as anotaacoes


senha_permitida = '1234'

while True:
    sistema = input('Digite [E] para ENTRAR!\nDigite [S] para SAIR! \n').upper()  # Converte a entrada para maiúsculas para facilitar a comparação
    if sistema == 'E':
        senha = input('Digite a senha: ')
        if senha == senha_permitida:
            print('Bem Vindo ao Sistema!')
            break
        else:
            print('Senha incorreta!')
    elif sistema == 'S':
        print('Saindo do sistema!')
        break
    else:
        print('Digite [E] para entrar ou [S] para sair!')

        
