import random


class Conta:
    def __init__(self, nome_titular, numero_conta, saldo) -> None:
        self.nome_titular = nome_titular
        self.numero_conta = numero_conta
        self.saldo = saldo

    def criar_conta(self):
        contas = {}
        contas[self.numero_conta] = {self.nome_titular, self.saldo}
        print(contas)
        # print(self.nome_titular)


# cria a conta 01

numero_gerado2 = random.randint(100, 1000)
nome = "samylle"
saldo = 0
conta01 = Conta(nome, numero_gerado2, saldo)

# cria a conta 02
numero_gerado = random.randint(100, 1000)
nome = "renan"
saldo = 0
conta02 = Conta(nome, numero_gerado, saldo)

# armazena as contas no dicionario
conta01.criar_conta()
conta02.criar_conta()
