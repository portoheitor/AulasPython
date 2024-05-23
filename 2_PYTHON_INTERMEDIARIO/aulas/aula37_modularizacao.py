
# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path

# o modulo so e carregado uma vez durante a exec do programa

# o modulo so é recarregado se vc solicitar
# import importlib
# importlib.reload(nome_modulo)



import aula37_modularizacao_mnodulo
from aula37_modularizacao_mnodulo import variavel_modulo,soma

print('Este módulo se chama', __name__)

print(aula37_modularizacao_mnodulo.variavel_modulo)
print(variavel_modulo)

print(aula37_modularizacao_mnodulo.soma(10,20))
print(soma(50,10))