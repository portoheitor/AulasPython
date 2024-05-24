"""
Enviando Mensagem Eletronica pelo PYTHON
"""

import os
import pathlib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template

from dotenv import load_dotenv

load_dotenv()

"""
Dados para acesar email/smtp e Destinatario
todos os dados vamos pegar das nossas variaveis em .evn para termos mais segurança
acesso via load_dotenv() e cpturando valor com os.getenv()
"""

email_remetente = os.getenv("FROM_EMAIL")
senha_remetente = os.getenv("EMAIL_PASSWORD")

destinatario_email = os.getenv("EMAIL_TESTS")

"""
Configurando SMTP
"""

smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = email_remetente
smtp_password = senha_remetente

"""
Criando/Capturando Mensagem a ser enviada,
Nesse caso vamos enviar um HTML, mas poderia ser
qualquer outro tipo de arquivo que possa ser enviado via email
"""

CAMINHO_MENSAGEM = pathlib.Path(__file__).parent / "aula22_email.html"

"""
Acessar arquivo para fazer o tratamento necessario antes de enviar
gero o conteudo, crio um template desse conteudo, e substituo a variavel
$nome do arquivo pelo nome apropriado/msg
"""

with open(CAMINHO_MENSAGEM, "r") as arquivo:
    conteudo = arquivo.read()
    template = Template(conteudo)
    conteudo_editado = template.substitute(nome="Desenvolvedor em Formação")

"""
Transformar em MIMEMultpart
-Qem esta enviando (from)
-Para quem enviar (to)
-Assunto Email (subject)
-Attach ( possibilidade de enviar varios formatos de anexos)
"""

mime_muiltpart = MIMEMultipart()
mime_muiltpart['from'] = email_remetente
mime_muiltpart['to'] = destinatario_email
mime_muiltpart['subject'] = "Teste de Envio de email Automatizado"

corpo_email = MIMEText(conteudo_editado, "html", "utf-8")

mime_muiltpart.attach(corpo_email)

"""
Conectar com o servidor SMTP
"""

with smtplib.SMTP(smtp_server, smtp_port) as server:
    server.ehlo()
    server.starttls()
    server.login(email_remetente, senha_remetente)
    server.send_message(mime_muiltpart)
    print('Email enviado!')