# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas tipos imutáveis como valor interno.

# Criando um set
# s1 = set()  # vazio
# s1 = {'Heitor', 1, 2, 3}  # com dados


# Sets são eficientes para remover valores duplicados de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1, 2, 3, 3, 3, 3, 3, 1]
# s1 = set(l1)  # com dados repetidos , os sets removem automaticamente os duplicados
# l2 = list(s1)
# print(s1)

# s1 = {1, 2, 3}
# print(3 in s1)
# print(4 in s1)
# for numero in s1:
#     print(numero)


# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('Heitor') #apenas um valor por vez
# s1.add(3)

# s1.update('ola mundo') #adiciona de forma interavel
# s1.update(('Hi world!', 1, 2, 3, 4)) # adiciona varios valores de uma so vez

# # s1.clear() #apaga o conteudo do set

# s1.discard('ola mundo') #remove o dado passado 
# print(s1)


# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 #uniao
s4 = s1 & s2 # intersecao (estao presentes em ambos conjuntos)
s5 = s1 - s2 # mostra apenas o dado que esta diferente na esquerda
s6 = s2 - s1
s7 = s1 ^ s2 #mostra a diferenca simetrica(itens que nao estao presentes apenas em um conjunto)

print(s3)
print(s4)
print(s5)
print(s6)
print(s7)


# Exemplo de uso dos sets
letras = set()
while True:
    letra = input('Digite: ')
    letras.add(letra.lower())

    if 'l' in letras:
        print('PARABÉNS')
        break

    print(letras)