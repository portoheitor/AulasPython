'''
crie um programa que passado uma string,apos cada char ele imprima
um "*" ex: Heitor -> H*e*i*t*o*r
'''


nome = 'Heitor Ribeiro Porto'
tamanho_nome = int(len(nome))

index = 0
nome_alterado = ''
while index < tamanho_nome:
    
    nome_alterado += f'*{nome[index]}'
    index += 1
       
print(nome_alterado)
    

       
