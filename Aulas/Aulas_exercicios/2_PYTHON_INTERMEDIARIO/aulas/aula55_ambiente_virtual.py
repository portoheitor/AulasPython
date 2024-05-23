# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

#ATIVAR AMBIENTE VIRTUAL
'''
CRIAR AMBIENTE
-> python3 -m venv nome_ambiente

ATIVAR AMBIENTE VIRTUAL

-> source venv/bin/activate

INSTALAR COM PIP

-> pip install nome_pacote
-> pip unistall nome_pacote -y

-> pip freeze   lista todas extensoes instaladas

REQUIREMENTS TXT
-> Gera novamente o venv ultilizado e manda para o repositorio
somente esse arquivo requirements.txt

pip freeze > requirements.txt

pip install -r requirements.txt  - assim recriamos o ambiente virtual

'''