"""
Higher Order Functions
Funções de primeira classe

-Atribuição a variáveis: Você pode atribuir uma função a uma variável.
-Passagem como argumentos: Você pode passar funções como argumentos para outras funções.
-Retorno de funções: Uma função pode retornar outra função como resultado.
-Armazenamento em estruturas de dados: Você pode armazenar funções em listas, dicionários, tuplas, etc.

Termos técnicos: Higher Order Functions e First-Class Functions

Academicamente, os termos Higher Order Functions e First-Class Functions têm significados diferentes.

    Higher Order Functions - Funções que podem receber e/ou retornar outras funções

    First-Class Functions - Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


print(
    executa(saudacao, 'Bom dia', 'Luiz')
)
print(
    executa(saudacao, 'Boa noite', 'Maria')
)