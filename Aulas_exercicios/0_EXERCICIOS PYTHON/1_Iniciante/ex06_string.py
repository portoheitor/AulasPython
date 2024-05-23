'''
Exercicio:

Peca ao usiario para digitar seu nome
Peca ao usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome e {nome}*
        Seu nome invertido é {nome invertido}*
        Seu nome contem (ou nao ) espacos*
        Seu nome tem {n} letras*
        A primeira letra do seu nome é {letra}*
        A ultima letra do seu nome é {letra}
Se nada for digitado em nome ou idade(ou se idade nao for um numero)
    exiba "Desculpe voce deixou campos vazios, ou preencheu incorretamente!"
'''

def is_number(inputs):
    try:
        float(inputs)
        return True
    except:
        return False

#quando faco *-1 ranformo em negativo, subtraindo 1 de um negativo chego ao final da string que é o tamanha total +1 no caso -10...-11.. dependendo da circunstancia e nome
def invert_name(name):
    try:
        if name != '' and is_number(name) == False:
            return name[-1:len(name) *-1 - 1:-1]
        else:
            return 'Campo preenchido incorretamente!'
    except:
        return False
    
def count_char(name):
    try:
        if name != '' and is_number(name) == False:
            name = len(name)
            return name
        else:
            return 'Campo preenchido incorretamente!'
    except:
        return False
    
def verify_spaces(name):
    try:
        if name != '' and is_number(name) == False:
            verificacao = ' '
            if verificacao in name:
                return True
            else:
                return False
        else:
            return 'Campo preenchido incorretamente!'
    except:
        return False

def primary_char(name):
    try:
        if name != '' and is_number(name) == False:           
            return name[0:1:1]
        else:
            return 'Campo preenchido incorretamente!'
    except:
        return False

def last_char(name):
    try:
        if name != '' and is_number(name) == False:            
            return name[len(name)-1:len(name):1]
        else:
            return 'Campo preenchido incorretamente!'
    except:
        return False


while True:
    nome = input('Digite seu nome: ')
    idade = input('qual sua idade? ')
    if (is_number(nome) == False and nome != '') and (is_number(idade) == True and idade != ''):
        print(f'Seu nome é = {nome}\n'
              f'Sua idade é = {idade}\n'
              f'Seu nome invertido é = {invert_name(nome)}\n'
              f'Seu nome contem espacos? = {verify_spaces(nome)}\n'
              f'Seu nome tem {count_char(nome)} letras\n'
              f'A Primeira letra do seu nome é = {primary_char(nome)}\n'
              f'A ultima letra do seu nome é = {last_char(nome)}')
        break
    else:
        print('Campos preenchidos incorretamente!')
        