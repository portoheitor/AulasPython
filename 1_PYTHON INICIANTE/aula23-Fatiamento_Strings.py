'''
Fatiamento deStrings

0123456789
ola mundo
-987654321

Fatiamento [i:f:p] (inicio, fim , passo(pular))

func len retorna a qntd de caracteres da str
'''

varialvel = 'Olá mundo'
print(len(varialvel) *-1 - 1)
print(varialvel[0:len(varialvel)])
print(varialvel[0:1:1])
print(varialvel[0:9:2])
print(varialvel[5:9:1])
print(varialvel[-1:len(varialvel) *-1 - 1:-1])