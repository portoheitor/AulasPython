'''
CONSTANTE = "Variaveis" que nao mudam

Muitas condicoes no mesmo if é RUIM
        <- contagem de complexidade ruim
'''

velocidade_carro = 50 #velocidade do carro
local_carro = 90 # localizacao do carro

RADAR_1 = 60 # Velocidade maxima radar1
LOCAL_1 = 100 # local onde radar1 esta
RADAR_RANGE = 1 # A distancia onde o radar pega

if velocidade_carro > RADAR_1:
    print(f'Carro passou a {velocidade_carro}km/h\nExcedeu limite de velocidade!')
elif velocidade_carro == RADAR_1:
    print(f'Carro Passou no limite maximo de velocidade {velocidade_carro}km/h!')
else:
    print(f'Carro passou a {velocidade_carro}km/h Abaixo do limite de velocidade!!')