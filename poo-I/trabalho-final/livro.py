class Livro:
    def __init__(
        self,
        codigo,
        preco,
        titulo,
        autor,
        genero,
    ) -> None:
        self._codigo = codigo
        self._preco = float(preco)
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._disponivel = True
        self._data_aluguel = None

    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        self._codigo = valor

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        self._preco = valor

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, valor):
        self._titulo = valor

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, valor):
        self._autor = valor

    @property
    def genero(self):
        return self._genero

    @genero.setter
    def genero(self, valor):
        self._genero = valor

    @property
    def disponivel(self):
        return self._disponivel

    @disponivel.setter
    def disponivel(self, valor):
        self._disponivel = valor

    @property
    def data_aluguel(self):
        return self._data_aluguel

    @data_aluguel.setter
    def data_aluguel(self, valor):
        self._data_aluguel = valor

    def documentacao():
        return (
            "A classe Livro representa um livro com informações sobre código, preço, título, autor, gênero, disponibilidade e data de aluguel.\n"
            "Atributos:\n"
            "- Código\n"
            "- Preço\n"
            "- Título\n"
            "- Autor\n"
            "- Gênero\n"
            "- Disponibilidade\n"
            "- Data de Aluguel\n"
            "Métodos:\n"
            "- documentacao() -> str\n"
        )
