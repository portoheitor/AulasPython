# Exercício - sistema de perguntas e respostas

# REFAZER

# def exibicao_perguntas():
#     contador_indice = []
#     contador_perguntas = []
#     perguntas_prontas = {}

#     for indice, pergunta in enumerate(perguntas):
#         contador_indice.append(indice)
#         contador_perguntas.append(pergunta['pergunta'])

#     for chave in range(len(contador_indice)):
#         perguntas_prontas[f'pergunta{chave}'] = contador_perguntas[chave]
    
#     return perguntas_prontas





# perguntas = exibicao_perguntas()

# for index in range(len(perguntas)):
#     print(perguntas[f'pergunta{index}'])
    
    
#     break

# Exercício - sistema de perguntas e respostas


perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou 👍')
    else:
        print('Errou ❌')

    print()


print('Você acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')