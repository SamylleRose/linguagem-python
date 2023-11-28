import datetime


class Conta:
    def __init__(self, titular, saldo) -> None:
        self.titular = titular
        self.saldo = float(saldo)
        self.historico = Historico()

    def extrato(self):
        self.titular.imprimir_cliente()
        print("Saldo:", self.saldo)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.add_transacao(
                f"Deposito de R${valor} realizado com sucesso!"
            )
            print("Deposito realizado com sucesso!")
        else:
            print("Não é possivel depositar um valor negativo!")

    def saque(self, saque):
        if saque > 0:
            if saque > self.saldo:
                print(f"Não é possivel sacar! seu saldo é de R${self.saldo}")

            else:
                self.saldo -= saque
                self.historico.add_transacao(
                    f"Saque de R${saque} realizado com sucesso!"
                )
        else:
            print(f"Não é possivel sacar! valor negativo!")

    def transferir(self, titular, destino, valor):
        if valor <= 0:
            print("valor negativo!")

        elif self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            self.historico.add_transacao(
                f"Transferencia para {titular} de R${valor} realizada com sucesso!"
            )
            print("Transferencia realizada com sucesso!")
        else:
            print("Sem saldo para a transferencia!")

    def imprimir_historico(self):
        self.historico.imprimir_transacoes()


class Cliente:
    def __init__(self, titular, cpf) -> None:
        self.titular = titular
        self.cpf = cpf

    def imprimir_cliente(self):
        print(f"cliente: {self.titular}")
        print(f"CPF: {self.cpf}")


class Historico:
    def __init__(self) -> None:
        self.data_criacao = datetime.datetime.now()
        self.transacoes = []

    def add_transacao(self, transacao):
        self.transacoes.append(str(datetime.datetime.now()) + "\n" + transacao)

    def imprimir_transacoes(self):
        print("Conta foi criada em: ", self.data_criacao)
        for transacoes in self.transacoes:
            print(transacoes)


# criar conta
cliente01 = Cliente("samylle", "243324")
cliente02 = Cliente("pedro", "1232143")

cliente01_conta = Conta(cliente01, 2000)
cliente02_conta = Conta(cliente02, 3000)

# depositar
# print("-" * 50)
# deposito = float(input("Digite um valor de deposito para a conta 02: "))
# cliente02_conta.depositar(deposito)
# print("\n")
# cliente02_conta.extrato()

# sacar
# print("-" * 50)
# sacar = float(input("Digite um valor de saque da conta 01: "))
# cliente01_conta.saque(sacar)
# print("\n")
# cliente01_conta.extrato()


# transferir
print("-" * 50)
valor_de_transferencia = float(
    input("Digite o valor para a tranferencia da conta 1 para a conta 2: ")
)

cliente01_conta.transferir(cliente02.titular, cliente02_conta, valor_de_transferencia)
cliente01_conta.extrato()
print("\n")
cliente02_conta.extrato()

# imprimir historico
print("-" * 50)
cliente01_conta.imprimir_historico()
print("\n")
cliente02_conta.imprimir_historico()
