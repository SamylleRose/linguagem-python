import random


class Conta:
    def __init__(self) -> None:
        self.contas = {}
        self.numeros_conta = [str(numero).zfill(3) for numero in range(0, 1000)]

    def gerar_numero_conta(self):
        numero_sorteado = -1

        if self.numeros_conta:
            numero_sorteado = random.choice(self.numeros_conta)
            self.numeros_conta.remove(numero_sorteado)

        return numero_sorteado

    def criar_conta(self, nome_titular):
        numero_conta = self.gerar_numero_conta()

        if numero_conta != -1:
            saldo = 0
            self.contas[numero_conta] = [nome_titular, saldo]

    def listar_contas(self):
        for numero_conta, lista_valores in self.contas.items():
            print("=" * 20)
            print(
                f"Numero da conta: {numero_conta}\nNome do titular: {lista_valores[0]}\nSaldo: {lista_valores[1]}\n"
            )

    def sacar_valor(self):
        self.listar_contas()

        conta_saque = input("Dígite o número da conta que deseja sacar: ")
        valor_saque = float(input("Dígite o valor do saque: "))

        if conta_saque not in self.contas.keys():
            print("\nEsta conta não existe!")

        elif valor_saque > self.contas[conta_saque][1]:
            print(
                "\nNão é possivel sacar esse valor, a conta possui apenas R${self.contas[conta_saque][1]}!"
            )
        else:
            self.contas[conta_saque][1] -= valor_saque
            print("\nSaque concluido com sucesso!")

    def depositar_valor(self):
        self.listar_contas()

        conta_deposito = input("Dígite o número da conta que deseja depositar: ")
        valor_deposito = float(input("Dígite o valor do deposito: "))

        if conta_deposito not in self.contas.keys():
            print("\nEsta conta não existe!")

        elif valor_deposito < 0:
            print("\nNão é possivel depositar um valor negativo!")

        else:
            self.contas[conta_deposito][1] += valor_deposito
            print("\nDeposito concluido com sucesso!")

    def transferir_valor(self):
        self.listar_contas()

        conta_origem = input("Digite o número da conta de origem: ")
        conta_destino = input("Digite o número da conta de destino: ")
        valor_transferencia = float(input("Dígite o valor da transferência: "))

        if (conta_origem not in self.contas.keys()) or (
            conta_destino not in self.contas.keys()
        ):
            print("\nA conta origem ou a conta destino não existe!")

        elif valor_transferencia > self.contas[conta_origem][1]:
            print(
                "\nNão é possivel sacar esse valor, a conta possui apenas R${self.contas[conta_saque][1]}!\n"
            )

        else:
            self.contas[conta_origem][1] -= valor_transferencia
            self.contas[conta_destino][1] += valor_transferencia

            print(
                f"\nValor R${valor_transferencia} saiu da conta {conta_origem} e foi transferido para conta {conta_destino}."
            )

    def excluir_conta(self):
        self.listar_contas()

        conta_excluir = input("Digite o número da conta que deseja excluir: ")

        if conta_excluir not in self.contas.keys():
            print("\nEsta conta não existe!")

        else:
            del self.contas[conta_excluir]
            print("Conta excluida com sucesso!")

    def menu(self):
        opcao = 0

        while opcao != 7:
            print("\n1-  Criar conta")
            print("2-  Listar contas")
            print("3-  Sacar valor")
            print("4-  Depositar valor")
            print("5-  transferir valor")
            print("6-  Excluir conta")
            print("7-  Cair")

            opcao = int(input("insira uma opção: "))
            print("\n")

            if opcao == 1:
                nome_titular = input("Digite o seu nome: ")
                self.criar_conta(nome_titular)

            elif opcao == 2:
                self.listar_contas()

            elif opcao == 3:
                self.sacar_valor()
            elif opcao == 4:
                self.depositar_valor()
            elif opcao == 5:
                self.transferir_valor()
            elif opcao == 6:
                self.excluir_conta()
            elif opcao != 7:
                print("Opção inválida!")


if __name__ == "__main__":
    conta = Conta()
    conta.menu()
