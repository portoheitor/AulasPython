'''
Crie uma funcao que multiplica todos os argumentos nao nomeados recebidos
Retorne o total para uma varial , e nmostre o valor da variavel

Crie uma funcao que fala se um numero é par ou impar 
Retorne se o numero é par ou impar
'''

def multiplicar(*args):
    try:
        total_para_multiplicar = []
        for numeros in args:
            if isinstance(numeros,(int, float)):
                total_para_multiplicar.append(numeros)
            else:
                print('Passe somente numeros para a funcao multiplicar')
                return ValueError
        
        total_multiplicado = 1
        for posicao in total_para_multiplicar:
            total_multiplicado *= posicao                       
            
        return total_multiplicado
    except:
        return False
    

def par_ou_impar(numero):
    try:        
        if isinstance(numero,(int, float)) == True:
            result = int(numero)
            if result % 2 == 0:
                print(f'O numero {result} é Par!')
                return True
            else:
                print(f'O numero {result} é Impar!')
                return True
        else:
            print(f'Passe somente numeros para verificacao de par ou impar!')
            return ValueError
                        
    except:
        return False
    

par_ou_impar(multiplicar(51,101,3,31))
    