"""
******************CALCULO PRIMEIRO DIGITO CPF****************
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7

***************CALCULO SEGUNDO DIGITO CPF*********************
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0

"""


VALIDAR_CPF = '746.824.890-70'

def confirma_primeiro_digito():
    MULTIPLICADORES_PRIMEIRO_DIGITO = 10
    
    cpf_fixed = []
    for digit in VALIDAR_CPF:
        if digit == '.' or digit == '-':
            continue
        else:
            cpf_fixed.append(int(digit))
    
    cpf_fixed.pop()
    cpf_fixed.pop()


    result_cpf_x_multiplicadores = []
    soma_resultado_multiplicacao = 0

    #Multiplicando cada digito do cpf
    for indice_cpf in cpf_fixed:
        result_cpf_x_multiplicadores.append(indice_cpf * MULTIPLICADORES_PRIMEIRO_DIGITO)
        MULTIPLICADORES_PRIMEIRO_DIGITO -= 1
    
    #Somando resultados da multiplicacao
    for result_mult in result_cpf_x_multiplicadores:
        soma_resultado_multiplicacao += result_mult

    result_final = (soma_resultado_multiplicacao * 10) % 11

    primeiro_digito = result_final if result_final < 9 else 0
    return primeiro_digito


def confirma_segundo_digito():
    MULTIPLICADORES_SEGUNDO_DIGITO = 11
    
    cpf_fixed = []
    for digit in VALIDAR_CPF:
        if digit == '.' or digit == '-':
            continue
        else:
            cpf_fixed.append(int(digit))
        
    cpf_fixed.pop()

    result_cpf_x_multiplicadores = []
    soma_resultado_multiplicacao = 0

    #Multiplicando cpf
    for indice_cpf in cpf_fixed:
        result_cpf_x_multiplicadores.append(indice_cpf * MULTIPLICADORES_SEGUNDO_DIGITO)
        MULTIPLICADORES_SEGUNDO_DIGITO -= 1

    #Somando resultados multiplicacao
    for result_mult in result_cpf_x_multiplicadores:
        soma_resultado_multiplicacao += result_mult

    result_final = (soma_resultado_multiplicacao * 10) % 11

    segundo_digito = result_final if result_final < 9 else 0
    
    return segundo_digito


print(confirma_primeiro_digito())
print(confirma_segundo_digito())

