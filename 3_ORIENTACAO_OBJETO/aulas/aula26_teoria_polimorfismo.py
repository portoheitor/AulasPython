# Polimorfismo em Python Orientado a Objetos
# Polimorfismo é o princípio que permite que
# classes deridavas de uma mesma superclasse
# tenham métodos iguais (com mesma assinatura)
# mas comportamentos diferentes.
# Assinatura do método = Mesmo nome e quantidade
# de parâmetros (retorno não faz parte da assinatura)
# Opinião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais
# SO"L"ID
# Princípio da substituição de liskov
# Objetos de uma superclasse devem ser substituíveis
# por objetos de uma subclasse sem quebrar a aplicação

#Sobrecarga de metodos (overlord) python NAO SUPORTA
#Sobreposicao de motodos (overrife) PYTHON NAO SUPORTA

from abc import ABC, abstractmethod


class Notificacao(ABC):
    def __init__(self, mensagem):
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...


class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print(f'E-mail: {self.mensagem}')
        return True


class NotificacaoSMS(Notificacao):
    def enviar(self):
        print(f'SMS: {self.mensagem}')
        return True


def notificar(notificacao: Notificacao):
    notificacao_enviada = notificacao.enviar()

    if notificacao_enviada:
        print('Notificacao Enviada')
    else:
        print('Notificacao Nao Enviada')


notificacao_email = NotificacaoEmail('Tete Email')
notificar(notificacao_email)

notificacao_sms = NotificacaoSMS('Teste SMS')
notificar(notificacao_sms)
