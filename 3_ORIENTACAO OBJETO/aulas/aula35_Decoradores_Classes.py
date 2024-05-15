# Classes decoradoras (Decorator classes)
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return self._multiplicador * resultado
        return interna


@Multiplicar(10)
def soma(x, y):
    return x + y


soma = soma(4, 2)
print(soma)

print()