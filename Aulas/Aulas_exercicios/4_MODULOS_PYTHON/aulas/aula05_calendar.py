# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo


import calendar

# print(calendar.calendar(2022)) anotodo
# print(calendar.month(2024,12)) somente mes

#ultimo dia do mes
#monthrange = retorna uma tupla com o nome do primeiro dia, e o numero do ultimo dia
#lembrando que o primeiro dia vai vir com o numero relativo ao dia da semana
# 0 = Monday | 1 = Tuesday | 2 = Wednesday | 3 = Thursday | 4 = Friday | 5 = Saturday | 6 = Sunday
print(calendar.monthrange(2024,12))

primeiro_dia, ultimo_dia = calendar.monthrange(2024, 12)

print('Primeiro dia: ', primeiro_dia, ' Numero representa o nome do dia da semana')
print('Ultimo dia: ',ultimo_dia)

#retorna o nome do dia de acordo com o numero do dia
print(calendar.day_name[calendar.weekday(2024,12,ultimo_dia)])

print('#########################################')
print()



