import abc


class Funcionario(abc.ABC):
    def __init__(self, nome, salario):
        self._nome = nome
        self._salario = salario

    @property
    def salario(self):
        return self._salario

    @property
    def nome(self):
        return self._nome

    @abc.abstractmethod
    def calcula_bonificacao(self):
        pass


class Gerente(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcula_bonificacao(self):
        return 0.15 * self.salario


class Secretario(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcula_bonificacao(self):
        return 0.1 * self.salario + 50


class Diretor(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)

    def calcula_bonificacao(self):
        return 0.3 * self.salario + 1000


class Controle_bonificacao:
    def __init__(self):
        self._total_bonificacao = 0

    def registra(self, f):
        if isinstance(f, Funcionario):
            self._total_bonificacao += f.calcula_bonificacao()
        else:
            print("Objeto não é funcionario!!!")


cb = Controle_bonificacao()
g = Gerente("Flavio", 1000)
f = Secretario("Henrique", 100)
d = Diretor("Joao", 500)

cb.registra(g)
cb.registra(f)
cb.registra(d)

print(cb._total_bonificacao)
