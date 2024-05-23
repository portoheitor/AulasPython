from pathlib import Path

caminho_projeto = Path()

# print(caminho_projeto.absolute())

caminho_arquivo = Path(__file__)
# print(caminho_arquivo)

criar_algo = caminho_arquivo.parent / "aula15"

# print(criar_algo / 'arquivo.txt')


arquivo = Path.home() / 'Desktop' / 'arquivo.txt'

#criar arquivo no sistema
arquivo.touch()
arquivo.write_text('ola Mundo')
print(arquivo.read_text())
#removerarquivo
arquivo.unlink()