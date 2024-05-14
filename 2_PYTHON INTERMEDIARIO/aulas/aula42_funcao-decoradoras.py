# Funções decoradoras são funções que decoram outras funções
# Decorar = Adicionar / Remover / REstringir / Alterar
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

# funcao DECORADORA recebe uma func e usa uma clousure para 'decorar' a funcao recebida

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna


def inverte_string(string):
    return string[::-1] #fatiamento de string


def e_string(parametro):
    if not isinstance(parametro, str):
        raise TypeError('parametro deve ser uma string')


inverte_string_checando_parametro = criar_funcao(inverte_string)
invertida = inverte_string_checando_parametro('123')
print(invertida)