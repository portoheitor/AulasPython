"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente -> metodo sacar
    ContaPoupanca -> metodo sacar

Pessoa (ABC)
    Cliente
        Clente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)

Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)

Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clentes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""

from Banco import Banco
from Cliente import Cliente
from Conta_Corrente import ContaCorrente
from Conta_Poupanca import ContaPoupanca

byt = Banco("BytBank")

byt.vincular_cliente(Cliente("Heitor", 30,"123.123.123-01",ContaCorrente()))
byt.vincular_cliente(Cliente("Arielle",29,"123.211.234-43",ContaPoupanca()))
byt.vincular_cliente(Cliente("Maite",1,"123.334.234-43",ContaCorrente()))


heitor = byt.manipular_conta_cliente("123.123.123-01")
maite = byt.manipular_conta_cliente("123.334.234-43")
arielle = byt.manipular_conta_cliente("123.211.234-43")

print(f"NomeCliente: {heitor.nome}\nConta: {heitor.conta} -> Saldo {heitor.conta.saldo}")
print("################")
print(f"NomeCliente: {maite.nome}\nConta: {maite.conta} -> Saldo {maite.conta.saldo}")
print("################")
print(f"NomeCliente: {arielle.nome}\nConta: {arielle.conta} -> Saldo {arielle.conta.saldo}")

