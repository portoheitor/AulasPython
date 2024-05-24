# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
import pathlib
#
# from pathlib import Path
# from PyPDF2 import PdfReader
#
# PASTA_RAIZ = Path(__file__).parent
# PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs_originais'
# PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'
#
# RELATORIO_BACEN = PASTA_RAIZ / 'R20240517.pdf'
#
# reader = PdfReader(str(RELATORIO_BACEN))
#
# page = reader.pages[0]
# count = 0
#
# for image_file_object in page.images:
#     with open(str(count) + image_file_object.name, "wb") as fp:
#         fp.write(image_file_object.data)
#         count += 1
