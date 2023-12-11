class Conta:
    __slots__ = ["_titular", "_saldo"]

    _total_contas = 0

    def __init__(self, _titular, _saldo) -> None:
        self._titular = _titular
        self._saldo = float(_saldo)
        Conta._total_contas += 1

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, saldo):
        self._saldo += saldo

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, titular):
        self._titular += titular

    def sacar(self, valor_saque):
        self._saldo -= valor_saque

    def depositar(self, valor_deposito):
        self._saldo += valor_deposito

    def transferir(self, destido_tranferencia, valor_transferencia):
        self._saldo -= valor_transferencia
        destido_tranferencia._saldo += valor_transferencia

    def extrato(self):
        self._titular.imprimir_cliente()
        print(f"Saldo: {self._saldo}")


class Cliente:
    def __init__(self, nome, cpf) -> None:
        self.nome = nome
        self.cpf = cpf

    def imprimir_cliente(self):
        print(f"Cliente: {self.nome}")
        print(f"CPF: {self.cpf}")


# cliente01 = Cliente("Fernando", "78283893142")
# cliente02 = Cliente("Marcelo", "39823973848")

# cliente01_conta = Conta(cliente01, 23)
# cliente02_conta = Conta(cliente02, 50)

# print("-" * 50)
# cliente01_conta.extrato()

# print("-" * 50)
# cliente01_conta.depositar(30)
# cliente01_conta.extrato()

# print("-" * 50)
# cliente01_conta.sacar(45)
# cliente01_conta.extrato()

# print("-" * 50)
# cliente01_conta.transferir(cliente02_conta, 10)
# cliente01_conta.extrato()

# contas = []

# contas.append(cliente01_conta)
# contas.append(cliente02_conta)

# contas[1].sacar(10)
# print(contas[1].saldo)


def menu():
    print(
        "1 - Adicionar contas\n2 - Exibir contas\n3 - Sacar\n4 - Depositar\n5 - Tranferir"
    )
    opcao = int(input("Digite uma opção:"))
    return opcao


def funcoes_menu():
    contas = []

    while True:
        opcao = menu()

        if opcao == 1:
            nome = input("Digite seu nome: ")
            cpf = input("Digite seu cpf: ")
            saldo = input("Digite seu saldo: ")

            cliente = Cliente(nome, cpf)
            cliente_conta = Conta(cliente, saldo)
            contas.append(cliente_conta)

            print("\nConta criada com sucesso!\n")
        elif opcao == 2:
            for c in contas:
                print("-" * 50)
                c.extrato()


# criar:N

# add Conta
# exibir contas
# sacar
# depositar
# tranferir
funcoes_menu()
