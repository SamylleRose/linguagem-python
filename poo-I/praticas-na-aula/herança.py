class Funcionario:
    def __init__(self, nome, matricula) -> None:
        self._nome = nome
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, nova_matricula):
        self._matricula = nova_matricula

    def imprimir(self):
        print(self._nome, "", self._matricula)


class Gerente(Funcionario):
    def __init__(self, nome, matricula, senha) -> None:
        super().__init__(nome, matricula)
        self._senha = senha

    def imprimir(self):
        print(super().nome, " ", super().matricula, " ", self._senha)


class Atendente(Funcionario):
    def __init__(self, nome, matricula, setor) -> None:
        super().__init__(nome, matricula)
        self._setor = setor

    def imprimir(self):
        print(super().nome, " ", super().matricula, " ", self._setor)


f1 = Funcionario("henrique", "123")
g1 = Gerente("pedro", "231", "897")
a1 = Atendente("fernando", "3242", "Caixa")

f1.imprimir()
g1.imprimir()
a1.imprimir()
