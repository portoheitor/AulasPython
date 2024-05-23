# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

caminho_arquivo = 'aula56.txt'

# arquivo = open(caminho_arquivo, 'w')
# #
# arquivo.close()

# o 'w' apaga o arquivo quando abri o mesmo e escreve somente oque esta no bloco
# with open(caminho_arquivo, 'w') as arquivo:
#        arquivo.write('Linha 1\n')
#        arquivo.write('Linha 2\n')
#        arquivo.writelines(
#            ('Linha 3\n', 'linha 4 \n')
#        )
#
# with open(caminho_arquivo, 'r') as arquivo:
#     # print(arquivo.read())
#     for linha in arquivo.readlines():
#         print(linha, end='')


with open(caminho_arquivo, 'a', encoding='utf8') as arquivo:
    arquivo.write('escrevendo no final do arquivo\n')


