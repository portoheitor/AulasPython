'''
Faca um programa que pergunte a hora ao usuario, e baseando-se no horario
descrito exiba uma saudacao apropriada. Ex:
        Bom dia 0:00 as 11:59, 
        Boa tarde 12:00 as 17:59
        Boa noite 18:00 as 23:59
'''


while True:  
    horario = input('Digite o horario atual: ')
    hora, minutos = horario.split(':')
    
    if hora.isdigit() and minutos.isdigit():
        hora = int(hora)
        minutos = int(minutos)
        if (hora >= 0 and hora <= 11) and (minutos >= 0 and minutos <= 59):
            print(f'Bom dia !\nHorario {hora}:{minutos}')
            break
        elif (hora >= 12 and hora <= 17) and (minutos >= 0 and minutos <= 59):
            print(f'Boa tarde!\nHorario {hora}:{minutos}')
            break
        elif (hora >= 18 and hora <= 23) and (minutos >= 0 and minutos <= 59):
            print(f'Boa noite!\nHorario {hora}:{minutos}')
            break
        else:
            print('Digite apenas numeros de horarios baseados no sistema 24hrs\nEX: 00:00 ate 23:59')
    else:
        print('Digite apenas NUMEROS de horarios baseados no sistema 24hrs\nEX: 00:00 ate 23:59')





   
