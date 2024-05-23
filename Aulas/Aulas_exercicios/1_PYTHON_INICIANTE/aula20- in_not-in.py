'''
operadorres in e not in

String sao iteraveis

indices: 

0 1 2 3 4 5
H e i t o r
-6 -5 -4 -3 -2 - 1

Podemos acessar qualquer char numa string usando o indice
tanto positivo quanto negativo
'''
# print(nome[2])
# print(nome[-4])

# print('ei' in nome)
# print('z' in nome)



nome = input('Digite seu nome : ')
encontrar = input('Digite oque deseja encontrar: ')

if encontrar in nome:
    print(f'"{encontrar}" foi encontrado em "{nome}"')