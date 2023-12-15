class Pessoa:
    def __init__(self, nome, idade) -> None:
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Agenda:
    total_pessoas_agenda = 0

    def __init__(self) -> None:
        self.pessoas = []

    def armazenaPessoa(self, nome, idade):
        if Agenda.total_pessoas_agenda < 10:
            nova_pessoa = Pessoa(nome, idade)
            self.pessoas.append(nova_pessoa)
            Agenda.total_pessoas_agenda += 1
            print("Armazenado com sucesso!")

        else:
            print("O máximo de pessoas na agenda foi atingido!")

    def removePessoa(self, nome):
        for pessoa in self.pessoas:
            if nome == pessoa.nome:
                self.pessoas.remove(pessoa)

    def buscaPessoa(self, nome):
        for pessoa in self.pessoas:
            if nome == pessoa.nome:
                print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade}")

    def imprimeAgenda(self):
        for pessoa in self.pessoas:
            print(pessoa.nome, pessoa.idade)


if __name__ == "__main__":
    agenda = Agenda()
    agenda.armazenaPessoa("Renan", 22)
    agenda.armazenaPessoa("Renan2", 23)
    agenda.imprimeAgenda()
    agenda.removePessoa("Renan")
    print("-" * 50)
    agenda.imprimeAgenda()
    print("-" * 50)
    agenda.buscaPessoa("Renan2")
