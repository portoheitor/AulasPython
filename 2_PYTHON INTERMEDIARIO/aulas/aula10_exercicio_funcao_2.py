'''
Crie funcoes que duplicam, triplicam e quadruplicam 
o numero passado como parametro
'''
def criar_multiplicador(multiplicdor):
    try:
        if isinstance(multiplicdor, (int, float)) == True:
            def multiplicar(numero):
                if isinstance(numero,(int, float)) == True:
                    return numero * multiplicdor
                else:
                    return f'Passe somente numeros para o valor a ser multiplicado!'
            return multiplicar
        else:
            return f'Passe somente numeros para o multiplicador'
    except ValueError:
        return f'Erro ao processar!'


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(10))
print(triplicar(10))
print(quadruplicar(10))

