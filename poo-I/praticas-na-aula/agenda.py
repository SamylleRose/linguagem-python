class Pessoa:
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade

    def imprimir_pessoa(self):
        print(self._nome, self._idade)

    @property
    def nome(self):
        return self._nome


class Agenda:
    def __init__(self) -> None:
        self._pessoas = []
        self._maxima = 5

    def armazenar(self, pessoa):
        if len(self._pessoa) < self._maximo:
            self._pessoas[pessoa.nome] = pessoa
            print("Pessoa adicionada")
        else:
            print("Agenda lotada!")

    def buscar(self, nome):
        for pessoa in self._pessoas:
            if nome == pessoa.nome:
                self._pessoas[nome].imprimir_pessoa()
                print("pessoa encontrada!")
            else:
                print("Pessoa não encontrada!")

    def revomer(self, nome):
        for pessoa in self.pessoas:
            if nome == pessoa.nome:
                self.pessoas.remove(pessoa)

    def printar(self):
        for nome in self.pessoas:
            self._pessoas[nome].imprimir_pessoa()


pessoa01 = Pessoa("fernando", 10)
pessoa02 = Pessoa("Dora", 6)

agenda_pessoa01 = Agenda(pessoa01)
agenda_pessoa02 = Agenda(pessoa02)
