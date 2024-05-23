# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html


from dataclasses import dataclass
from dataclasses import asdict, astuple, dataclass,field


@dataclass(frozen= True)
class Pessoa:
    nome: str = field(default= 'Missing')
    sobrenome: str = field(default= 'Not')
    idade: int = field(default= 0)
    enderecos: list[str] = field(default_factory= list)

    # def __post_init__(self):
    #    self.nome_completo = f"{self.nome} {self.sobrenome}"


if __name__ == '__main__':
    p1 = Pessoa()
    print(p1)
    # print(asdict(p1).keys())
    # print(asdict(p1).values())
    # print(asdict(p1).items())
    # print(astuple(p1)[0])
