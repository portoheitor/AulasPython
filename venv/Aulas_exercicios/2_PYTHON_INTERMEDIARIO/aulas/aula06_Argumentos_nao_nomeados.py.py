'''
args - Argumentos nao nomeados

* - *args (empacotamentos e desempacotamento)
'''

#lembrando desempacotamento
# x, y, *resto = 1, 2, 3, 4
# print(x,y,resto)

def soma(*args):
    try:
        total = 0
        for nums in args:
            if isinstance(nums,(int, float)):
                total += nums
            else:
                print('Passe apenas numeros para funcao soma')
                return ValueError
        return total
    except ValueError:
        return ValueError
    
   
   


numeros = 1,2,3,'a',10,50,55
soma_numeros = soma(*numeros)

soma1 = soma(1,2,5,10)
print(soma_numeros)
print(soma1)