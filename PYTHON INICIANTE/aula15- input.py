def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


nome_user = input('Qual seu nome? ')

while True:
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro numero: ')

    if is_number(num_1) and is_number(num_2):
        int_num_1 = int(num_1)
        int_num_2 = int(num_2)
        print(f'Bem vindo {nome_user}!\nA soma dos números é: {int_num_1 + int_num_2}')
        break
    else:
        print("Por favor, digite números válidos. Tente novamente.")
