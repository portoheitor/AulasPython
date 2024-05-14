# Introdução às Generator functions em Python
# generator = (n for n in range(1000000))

#Generator pausao ao inves de simplistemente dar um retorn e finalizar a execucao
# pode usar a palavra yild (e o 'return') porem PAUSA a execusao e guarda o valor no next


def generator(n=0, maximum=10):
    while True:
        yield n #pausar
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    print(n)