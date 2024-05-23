"""
Reultilizamos o codigo do ex16
objetivo é salvar os itens da lista em 1 arquivo.json
"""
import json

CAMINHO_ARQUIVO = 'aula59_salvar_lista.json'


def add_item_lista(mensagem, lista):
    lista.append(mensagem)
    print(f'Tarefa adicionada: {mensagem}')


def remove_ultima_tarefa(lista, lista_backup):
    if not lista:
        print('NENHUMA TAREFA PARA REMOVER')
    else:
        tarefa = lista.pop()
        lista_backup.append(tarefa)


def refazer_ultima_tarefa(lista, lista_backup):
    if not lista_backup:
        print('NENHUMA TAREFA A REFAZER')
    else:
        tarefa_refazer = lista_backup.pop()
        lista.append(tarefa_refazer)

def tarefas_salvas(caminho):
    ler_json(caminho)

def exibir_lista(lista):
    if not lista:
        print('NENHUMA TAREFA A SER EXIBIDA')
    else:
        for tarefa in lista:
            print(f'-> {tarefa}')


def verifica_mensagem(msg_usuario):
    if not msg_usuario.isdigit():
        return True
    else:
        raise TypeError(
            f'"{msg_usuario} deve ser uma String!\nEx: -> Nadar -> Listar'
        )


def processamento_listagem(mensagem, lista, lista_backup):
    if mensagem == 'listar':
        exibir_lista(lista)


    elif mensagem == 'desfazer':
        remove_ultima_tarefa(lista, lista_backup)

    elif mensagem == 'refazer':
        refazer_ultima_tarefa(lista, lista_backup)

    elif mensagem == 'salvos':
        tarefas_salvas(CAMINHO_ARQUIVO)

    elif mensagem == 'sair':
        raise StopIteration

    else:
        add_item_lista(mensagem, lista)
        salva_json(lista, CAMINHO_ARQUIVO)
    return lista


def salva_json(lista, caminho_arquivo):
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        json.dump(lista, arquivo, indent=2, ensure_ascii=False)


def ler_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não existe')
        salva_json(lista, caminho_arquivo)
    return exibir_lista(dados)


lista = []
lista_backup = []

while True:
    print(f'Digite um Comando ou tarefa!')
    mensagem = input('Comandos: Listar -> Desfazer -> Refazer -> Salvos -> Sair\n Digite: ')
    mensagem_minuscula = mensagem.lower()

    try:
        verifica_mensagem(mensagem)
        lista = processamento_listagem(mensagem_minuscula, lista, lista_backup)
        print()

    except StopIteration as e:
        print(f'Saindo{e}')
        break