'''
Listas em python
Tipo list - Mutavel
Suporta varios valores de qualquer tipo
Conhecimentos reutilizaveis - Indices e Fatiamento
Metodos uteis:  append, insert, pop, del, clear, extend, +
                Create Read update Delete
                Criar, ler, alterar, apagar = lista[i](CRUD)
                
            OBS : EVITE MOVER OS INDICES DESTA LISTA
                  SEMPRE TENTAR RETIRAR O ULTIMO ITEM DA LISTA PARA EVITAR LENTIDAO
 
 
    append - Adiciona um item ao final da lista
    insert - Adiciona um item no indice escolhido
    pop    - Remove um item do final ou indice escolhido
    del    - Apaga um indice
    clear  - Limpa a lista
    extend - Estente a lista
    +      - Concatena listas
 '''

#        0     1          2         3    4
#        -5   -4         -3         -2   -1
# lista = [123, True, 'Heitor Porto', 1.2, []]
# lista[-3] = 'Maite'

# print(lista[2].upper(), type(lista[2]))

# lista = [10, 20, 30, 40]
# lista[2] = 300
# print(lista)
# del lista[2]
# print(lista)

lista = [10, 20, 30, 40]
lista.append(50) #adiciona um dado ao ultimo indice da lista

print(lista)

ultimo_valor = lista.pop() # remove o ultimo elemento

print(lista, 'Removendo', ultimo_valor)