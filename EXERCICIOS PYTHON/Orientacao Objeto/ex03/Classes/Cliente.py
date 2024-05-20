from Pessoa import Pessoa
class Cliente(Pessoa):
    def __init__(self, nome:str, idade:int):
        super().__init__()
        self.nome = None
        self.idade = None
        self._conta_corrente = False
        self._conta_poupanca = False

    @property
    def conta_corrente(self):
        return self._conta_corrente
    @property
    def conta_poupanca(self):
        return self._conta_poupanca

