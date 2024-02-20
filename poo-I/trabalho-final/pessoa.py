from abc import ABC


class Pessoa(ABC):
    def __init__(self, nome, cpf) -> None:
        self._nome = nome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome += valor
        return self._nome

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        self._cpf += valor
        return self._cpf
