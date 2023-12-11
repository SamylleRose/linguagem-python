from datetime import datetime


class Pessoa:
    def __init__(self, nome, data_de_nascimento, altura) -> None:
        self._nome = nome
        self._data_de_nascimento = data_de_nascimento
        self._altura = altura

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, novo_nome) -> None:
        self._nome = novo_nome

    @property
    def data_de_nascimento(self) -> datetime:
        return self._data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, nova_data_de_nascimento) -> None:
        self.data_de_nascimento = nova_data_de_nascimento

    @property
    def altura(self) -> float:
        return self.altura

    @altura.setter
    def altura(self, nova_altura) -> None:
        self.altura = nova_altura

    def imprimir_dados(self) -> None:
        data_formatada = self._data_de_nascimento.strftime("%d/%m/%Y")
        print(f"Nome: {self._nome}")
        print(f"Data de Nascimento: {data_formatada}")
        print(f"Altura: {self._altura} metros")

    def calcular_idade(self) -> int:
        data_atual = datetime.now()
        ano_atual = data_atual.year
        ano_nascimento = self._data_de_nascimento.year
        idade = ano_atual - ano_nascimento

        if (data_atual.month, data_atual.day) < (
            self._data_de_nascimento.month,
            self._data_de_nascimento.day,
        ):
            idade -= 1

        return idade


# Exemplo de uso da classe
pessoa1 = Pessoa("João", datetime.strptime("11/10/2002", "%d/%m/%Y"), 1.75)

# Imprime os dados da pessoa
pessoa1.imprimir_dados()

# Imprime a idade da pessoa
print(f"Idade: {pessoa1.calcular_idade()} anos")
