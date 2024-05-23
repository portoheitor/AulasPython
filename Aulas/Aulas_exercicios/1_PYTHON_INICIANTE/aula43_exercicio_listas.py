'''
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de:
    ISERIR, APAGAR e LISTAR VALORES da lista
    
Nao permita que o programa quebre com erros de indices inexistentes
'''
lista_de_compras = []

def inserir_item(item):
    try:
        if not isinstance(item, str):
            print('Insira somente o nome do item como uma string!')
        else:
            lista_de_compras.append(item)         
            print()
    except Exception as e:
        print(f'Erro ao adicionar item à lista de compras: {e}')

def remover_item(indice):
    try:
        if not isinstance(indice, int):
            print('Insira somente o Indice do item que deseja remover!')
        else:
            lista_de_compras.pop(indice)
            print()
    except Exception as e:
        print(f'Erro ao remover item da lista de compras: {e}')

def mostrar_itens_lista():
    try:
        for indice, nome in enumerate(lista_de_compras):
            print(indice, nome)
        
        print()
    except Exception as e:
        print(f'Erro ao exibir lista de compras: {e}')
        
while True:
    alternativas = input(f'Para Adicionar um item a Lista digite [A]\n'
                        f'Para Mostrar os item da Lista digite [M]\n'
                        f'Para Remover um item da Lista digite [R]\n'
                        f'Para Sair da Lista digite [S]\n')

    if not isinstance(alternativas, str):
        print('Digite apenas os idices indicados!')
        continue
    else:
        alternativas = alternativas.upper()
        
    if alternativas == 'A':
        item_para_adicionar = input('Digite o item para Adicioanr a lista: ')
        if not isinstance(item_para_adicionar, str):
            print('Digite apenas Palavras para Adicionar a  lista')
        else:
            inserir_item(item_para_adicionar)
            continue
    elif alternativas == 'M':
        print('Lista de Itens: ')
        mostrar_itens_lista()
        continue
    elif alternativas == 'R':
        indice = input('Digite o indice do intem que deseja Remover: ')
        if not isinstance(indice, int):
            print('Digite apenas o numero do indice do item que sera removido!')
        else:
            remover_item(indice)
            continue
    elif alternativas == 'S':
        print('Finalizando Programa!')
        break