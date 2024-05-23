'''
faca um programa que mostre qual letra apareceu mais vezes naa frase
-percorra a frase olhando verificando cada letra
-guarde a letra atual para comparar e contar
- se a letra for 'ESPACO' pule
- conte a qnt de vezes que a letra apareceu

'''

frase = 'O Python é uma linguagem de programacao '\
    'multiparadigma. '\
        'Python foi criado por Guido Van Rossum.'
        
i = 0
qnt_apareceu_mais_vezes = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]
    
    if letra_atual == ' ':
        i += 1
        continue
    
    qntd_atual = frase.count(letra_atual)
    
    if qnt_apareceu_mais_vezes < qntd_atual:
        qnt_apareceu_mais_vezes = qntd_atual
        letra_apareceu_mais = letra_atual
        
    i += 1

print(f'A letra que mais apareceu na Frase:\n"{frase}"\nFoi a letra "{letra_apareceu_mais}", que apareceu {qnt_apareceu_mais_vezes}x')