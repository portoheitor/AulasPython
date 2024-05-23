from Cliente import Cliente
from Conta_Corrente import ContaCorrente
from Conta_Poupanca import ContaPoupanca


class Banco:
    def __init__(self, nome: str):
        self._nome_banco = nome
        self._clientes: list[Cliente] = []  #substituir por Banco de Dados em breve

    def exibir_clientes(self):
        for clientes in self._clientes:
            print(clientes)

    def vincular_cliente(self, cliente: Cliente):
        # uniao = {cliente}
        self._clientes.append(cliente)

    def manipular_conta_cliente(self, cpf:str):
        try:
            for conta in self._clientes:
                if conta.cpf == cpf:
                    return conta
                else:
                    continue
        except Exception as error:
            raise error.args


    def __repr__(self):
        class_name = type(self).__name__
        attrs = (f'Clientes: {self._clientes!r}')
        return f'{class_name} -> {self._nome_banco!r} {attrs}'
