# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print('ABRIR ARQUIVO')
    # 8/0
except Exception as error:
    print('MSG: ',error.__class__.__name__)
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')