'''
Crie uma calculadora de operacoes basicas com while
+ - / * 
'''

def soma(num_a, num_b):
    num_a = float(num_a)
    num_b = float(num_b)
    return num_a + num_b

def subtracao(num_a, num_b):
    num_a = float(num_a)
    num_b = float(num_b)
    return num_a - num_b

def divisao(num_a, num_b):
    num_a = float(num_a)
    num_b = float(num_b)
    return num_a / num_b

def multiplicacao(num_a, num_b):
    num_a = float(num_a)
    num_b = float(num_b)
    return num_a * num_b

def calculadora_simples():
    try:
        while True:
            operacao = input('Para Somar digite [+]\nPara SUBTRAIR digite [-]\nPara DIVIDIR digite [/]\nPara MULTIPLICAR digite [*]\n')
            if operacao.isdigit() != True and operacao == '+':
                num_a = input('Digite um numero: ')                       
                num_b = input('Digite outro numero: ')
                if (num_a.isdigit() == True) and (num_b.isdigit() == True):
                    print(f'A soma de {num_a} + {num_b} = {soma(num_a, num_b)}\n')
                    break
                else:
                   print('Digite apenas numeros!')
            elif operacao.isdigit() != True and operacao == '-':
                num_a = input('Digite um numero: ')                       
                num_b = input('Digite outro numero: ')
                if (num_a.isdigit() == True) and (num_b.isdigit() == True):
                    print(f'A Subtracao de {num_a} e {num_b} = {subtracao(num_a, num_b)}\n')
                    break
                else:
                    print('Digite Apenas Numeros!')
            elif operacao.isdigit() != True and operacao == '/':
                num_a = input('Digite um numero: ')                       
                num_b = input('Digite outro numero: ')
                if (num_a.isdigit() == True) and (num_b.isdigit() == True):
                    print(f'A Divisao de {num_a} e {num_b} = {divisao(num_a, num_b)}\n')
                    break
                else:
                    print('Digite Apenas Numeros!')
            elif operacao.isdigit() != True and operacao == '*':
                num_a = input('Digite um numero: ')                       
                num_b = input('Digite outro numero: ')
                if (num_a.isdigit() == True) and (num_b.isdigit() == True):
                    print(f'A Multiplicacao de {num_a} e {num_b} = {multiplicacao(num_a, num_b)}\n')
                    break
                else:
                    print('Digite Apenas Numeros!')
            else:
                print('Digite apenas a Operacao que deseja!')           
    except:
        return False
    

print('Bem Vindo!\nEsta é uma Calculadora de Operacoes Simples (+ - / *)!')
condicao = True
while condicao:
    entrada_saida = input('Para Abrir a Calculadora Digite [E]\nPara Sair do Programa digite [S]\n')
    entrada_saida = str.upper(entrada_saida)
    
    if entrada_saida.isdigit() != True and entrada_saida == 'S':
        print('Finalizando Programa!')
        break
    elif entrada_saida.isdigit() != True and entrada_saida =='E':
        calculadora_simples()
        while True:
            continuacao = input('Para Ralizar outra operacao Digite [C]\nPara Voltar ao menu inicial [I]')
            continuacao = str.upper(continuacao)
            if continuacao.isdigit() != True and continuacao == 'C':
                calculadora_simples()
            elif continuacao.isdigit() != True and continuacao == 'I':
                print('Finalizando Programa')
                break            
            else:
                print('Digite apenas o valor indicado!\n')        
    else:
        print('Digite apenas os valores indicados!')
    
    