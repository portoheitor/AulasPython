'''
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de:
    ISERIR, APAGAR e LISTAR VALORES da lista
    
Nao permita que o programa quebre com erros de indices inexistentes
'''
import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir\n[a]pagar\n[l]istar\n[s]air\n')

    if opcao == 'i':
        os.system('clear')
        valor = input('Valor a ser adicionado: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input(
            'Escolha o índice para apagar: '
        )

        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número int.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('clear')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    elif opcao == 's':
        print('Finalizando Programa!')
        break
    else:
        print('Por favor, escolha i, a, l ou s.')