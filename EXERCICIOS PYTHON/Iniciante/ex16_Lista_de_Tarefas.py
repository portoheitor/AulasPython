"""
Crie um programa que permita que voce adicione Tarefas a uma lista
Liste essas tarefas
remova a última tarefa adicionada
adicione novamente a tarefa removida
"""


def add_item_lista(mensagem, lista):
    lista.append(mensagem)
    print(f'Tarefa adicionada: {mensagem}')


def remove_ultima_tarefa(lista, lista_backup):
    tarefa = lista.pop()
    lista_backup.append(tarefa)


def refazer_ultima_tarefa(lista, lista_backup):
    tarefa_refazer = lista_backup.pop()
    lista.append(tarefa_refazer)


def exibir_lista(lista):
    for tarefa in lista:
        print(f'-> {tarefa}')


def processamento_listagem(mensagem, lista, lista_backup):
    if mensagem == 'listar':
        exibir_lista(lista)

    elif mensagem == 'desfazer':
        remove_ultima_tarefa(lista, lista_backup)

    elif mensagem == 'refazer':
        refazer_ultima_tarefa(lista, lista_backup)

    elif mensagem == 'sair':
        return False

    else:
        add_item_lista(mensagem, lista)
    return lista


def verifica_mensagem(msg_usuario):
    if not msg_usuario.isdigit():
        return True
    else:
        raise TypeError(
            f'"{msg_usuario} deve ser uma String!\nEx: -> Nadar -> Listar'
        )


lista = []
lista_backup = []
while True:
    print(f'Digite um Comando ou tarefa!')
    mensagem = input('Comandos: Listar -> Desfazer -> Refazer -> Sair\n Digite: ')
    mensagem_minuscula = mensagem.lower()

    try:
        verifica_mensagem(mensagem)
        lista = processamento_listagem(mensagem_minuscula, lista, lista_backup)
        print()
        if not lista:
            break
    except TypeError as e:
        print(f'Erro: {e}')
