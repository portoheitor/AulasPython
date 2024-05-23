from Pessoa import Pessoa
from Conta_Corrente import ContaCorrente
from Conta_Poupanca import ContaPoupanca


class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int, cpf: str, conta: ContaCorrente | ContaPoupanca):
        super().__init__(nome, idade, cpf)
        self._conta = conta

    @property
    def conta(self):
        return self._conta
    @conta.setter
    def conta(self,conta):
        self._conta = conta

    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}'

   

if __name__ == "__main__":
    cl = Cliente("Heitor",30,"123.234.234-43",ContaCorrente())
    cl2 = Cliente("AMite",12,"123.212.234-43",ContaPoupanca())
    cl3 = Cliente("Maite",1,"123.334.234-43",ContaCorrente())
    cl4 = Cliente("Arielle",29,"123.211.234-43",ContaPoupanca())

    print(cl.nome, cl.idade, cl.conta)
    print(cl2.nome, cl2.idade, cl2.conta)
    print(cl3.nome, cl3.idade, cl3.conta)
    print(cl4.nome, cl4.idade, cl4.conta)
