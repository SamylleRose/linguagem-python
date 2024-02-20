from pessoa import Pessoa


class Bibliotecario(Pessoa):
    def __init__(self, nome, cpf, senha) -> None:
        super().__init__(nome, cpf)
        self._senha = senha

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        self._senha += valor
        return self._senha

    def documentacao():
        return (
            "A classe Bibliotecario representa um bibliotecário e herda características da classe Pessoa.\n"
            "Atributos:\n"
            "- Nome (herdado da classe Pessoa)\n"
            "- CPF (herdado da classe Pessoa)\n"
            "- Senha (atributo específico da classe Bibliotecario)\n"
            "Métodos:\n"
            "- documentacao() -> str\n"
        )
