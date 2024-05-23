# Problema dos parâmetros mutáveis em funções Python
# Nunca chamar uma funcao com um parametro mutável
# ex: def adiciona_clientes(nome, lista =[])
# jamais faca isso, pois o python nao vai distinguir as listas se nao for passada nada
# como parametro da funcao
# como for definir um valor PADRÃO, nunca USAR um MUTÁVEL

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciona_clientes('luiz')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
cliente1.append('Edu')

cliente2 = adiciona_clientes('Helena')
adiciona_clientes('Maria', cliente2)

cliente3 = adiciona_clientes('Moreira')
adiciona_clientes('Vivi', cliente3)

print(cliente1)
print(cliente2)
print(cliente3)
