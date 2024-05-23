# iterator so sabe entregar o proximo valor e ao final levanta um StopIterator
# nao tem como fazer mais de um for em um iterator( tem que criar umas lista ....)

import sys

iterable = ['Eu',  'Tenho', '__iter__']

iterator = iter(iterable)   # tem __iter__ e __next__

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))


# Generator Expression sao funcoes que sabem pausar em determinadas ocasioes
#  todo generator é um iterator , mas um iterator nao é um generator
# o generator nao salva todo o conteudo na memoria, ele deixa pausado o iterator ate vc pedir
# para o next para avancar nesse generator
# nao tem tamanho, nao tem indice , nao tem nenhum caracteristica da lista


lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))
