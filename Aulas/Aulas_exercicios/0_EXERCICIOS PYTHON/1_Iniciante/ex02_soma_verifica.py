'''
Crie um programa que peça dois números ao usuário e imprima a soma deles
'''


def is_number(inputs):
    try:
        float(inputs)
        return True
    except:
        return False

def soma(*args):
    
    resultado = 0

    for numero in args:
        resultado += numero

    return resultado
    

while True:
    number_1 = input('Digite um numero: ')
    number_2 = input('Digite outro numero: ')
    if is_number(number_1) and is_number(number_2):
        
        result_soma = soma(float(number_1), float(number_2))
        
        print(f'A Soma dos numeros é = {result_soma}')
        break
    else:
        print('Digite somente NUMEROS!\nTente Novamente...')