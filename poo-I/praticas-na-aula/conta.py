class Conta:
    def __init__(self, titular, saldo) -> None:
        self.titular = titular
        self.saldo = float(saldo)

    def extrato(self):
        # print("Titular:", self.titular)
        self.titular.imprimir_cliente()
        print("Saldo:", self.saldo)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor

        else:
            print("Não é possivel depositar um valor negativo!")

    def saque(self, saque):
        if saque > self.saldo:
            print(f"Não é possivel sacar! seu saldo é de {self.saldo}")

        else:
            self.saldo -= saque

    def transferir(self, destino, valor):
        if valor > 0:
            return False, "valor negativo!"
        elif self.saldo >= valor:
            self.saldo -= valor
            destino.saldo += valor
            return True, "Transferencia realizada com sucesso!"
        else:
            print("Sem saldo para a transferencia!")


class Cliente:
    def __init__(self, titular, cpf) -> None:
        self.titular = titular
        self.cpf = cpf

    def imprimir_cliente(self):
        print(f"cliente: {self.titular}")
        print(f"CPF: {self.cpf}")


cliente01 = Cliente("samylle", "243324")
cliente02 = Cliente("pedro", "1232143")

cliente01_conta = Conta(cliente01, 2000)
cliente02_conta = Conta(cliente02, 3000)

# print(c1.titular)
# print(c2.titular)
# deposito = float(input("Digite um valor de deposito: "))
# c2.depositar(deposito)
# c2.extrato()

# sacar = float(input("Digite um valor de saque: "))

# c2.saque(sacar)
cliente01_conta.extrato()
cliente02_conta.extrato()

# valor_de_transferencia = float(
#     input("Digite o valor para a tranferencia da conta 1 para a conta 2: ")
# )

# c1.transferir(c2, valor_de_transferencia)
# c1.extrato()
# c2.extrato()
