from datetime import datetime


class Historico:
    formato_brasileiro = "%d/%m/%Y %H:%M:%S"

    def __init__(self, mensagem_inicial="Histórico: \n") -> None:
        self._historico = mensagem_inicial

    @property
    def historico(self):
        return self._historico

    @historico.setter
    def historico(self, valor):
        self._historico = valor

    def mostrar(self):
        return self._historico

    def adicionar(self, novo_historico):
        self._historico += (
            datetime.now().strftime(Historico.formato_brasileiro)
            + "\t"
            + novo_historico
            + "\n"
        )

    def documentacao():
        return (
            "A classe Historico representa um histórico de mensagens com registro de data e hora.\n"
            "Atributos:\n"
            "- historico (parâmetro opcional no construtor)\n"
            "Métodos:\n"
            "- mostrar() -> str\n"
            "- adicionar(novo_historico: str) -> None\n"
            "- documentacao() -> str\n"
            "Formato brasileiro de data e hora utilizado: '%d/%m/%Y %H:%M:%S'\n"
        )
