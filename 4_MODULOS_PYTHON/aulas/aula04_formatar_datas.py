# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html
from datetime import datetime

# data = datetime(2022, 12, 13, 7, 59, 23)
data = datetime.strptime('2024-12-13 07:59:23', '%Y-%m-%d %H:%M:%S')
print(data)
print()
print(data.strftime('%d/%m/%Y'))
print()
print(data.strftime('%d/%m/%Y %H:%M'))
print()
print(data.strftime('%d/%m/%Y %H:%M:%S'))
print()
#Pegar somente dados
print(data.strftime('%Y'), data.year)
print()
print(data.strftime('%d'), data.day)
print(data.strftime('%m'), data.month)
print()
print(data.strftime('%H'), data.hour)
print()
print(data.strftime('%M'), data.minute)
print()
print(data.strftime('%S'), data.second)