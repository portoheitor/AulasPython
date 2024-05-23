'''
Faça um programa que converta uma temperatura em Celsius para Fahrenheit. A fórmula é: Fahrenheit = (Celsius * 9/5) + 32.
'''

import requests

city = 'Ouro Fino,MG,BR'
api_key = '426954901a2cd4eb889fc315c0b08b2e'

def get_get_temperatura(city_name, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    get_temperatura = data['main']['temp']
    return get_temperatura


get_temperatura = get_get_temperatura(city, api_key)

convert_fahrenheint = (get_temperatura * 9/5) + 32
print(f'A temperatura em Ouro Fino, MG é {get_temperatura}°C.\nConvertendo em Fahrenheit a Temperatura é de : {convert_fahrenheint}°F.')


