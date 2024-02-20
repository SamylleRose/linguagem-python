from historico import Historico
from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, nome, cpf) -> None:
        super().__init__(nome, cpf)
        self._historico = Historico()

    @property
    def livros_alugados(self):
        return self._livros_alugados

    @livros_alugados.setter
    def livros_alugados(self, valor):
        self._livros_alugados = valor

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, valor):
        self._historico = valor

    def documentacao():
        return (
            "A classe Cliente representa um cliente e herda características da classe Pessoa.\n"
            "Atributos:\n"
            "- Nome (herdado da classe Pessoa)\n"
            "- CPF (herdado da classe Pessoa)\n"
            "- Histórico (atributo específico da classe Cliente)\n"
            "Metodos:\n"
            "- documentacao() -> str\n"
        )
