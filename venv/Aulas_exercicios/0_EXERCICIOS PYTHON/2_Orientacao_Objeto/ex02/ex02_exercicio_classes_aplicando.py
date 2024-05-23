from ex02_exercicio_classes import FabricarCarro

fusca = FabricarCarro('Wolks', 'Fusca', 'Boxer 1600')
print(fusca.caracteristicas)
fusca.motor = 'Boxer Turbo 2.0'
print(fusca.caracteristicas)

uno = FabricarCarro('Fiat', 'Uno-Escada', 'v8 Encapetado')
print(uno.caracteristicas)
