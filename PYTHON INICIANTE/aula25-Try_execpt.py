'''
Introducao ao try/execpt

try -> tenta executar oi codigo

except -> ocorreu algum erro ao tentar executar
'''

numero_str = input('Digite um numero para dobrar: ')


try:
    numero_float = float(numero_str)
    print(f'O dobro de {numero_float} é {numero_float *2:.2f}')
except:
    print('Isso nao é um numero ')