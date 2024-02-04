from random import choice


from history import History
from client import Client
from account import CurrentAccount, SavingsAccount, LifeInsurance
from taxation import Taxation

Taxation.register(CurrentAccount)
Taxation.register(LifeInsurance)

taxation_classes = [CurrentAccount, LifeInsurance]

for taxation_class in taxation_classes:
    if not hasattr(taxation_class, "calculate_taxation"):
        raise Exception("Interface not implemented")


class Bank:
    account_numbers = [str(number).zfill(4) for number in range(0, 10000)]
    total_accounts = 0
    taxations = []

    def __init__(self):
        self._clients = []

    @property
    def clients(self):
        return self._clients

    @clients.setter
    def clients(self, value):
        self._clients += value

    @classmethod
    def generate_account_number(cls):
        chosed_number = -1

        if cls.account_numbers:
            chosed_number = choice(cls.account_numbers)
            cls.account_numbers.remove(chosed_number)

        return chosed_number

    @classmethod
    def increment_total_account(cls):
        cls.total_accounts += 1

    def cpf_already_exists(self, cpf):
        result = False

        size = len(self.clients) - 1
        while size >= 0 and result == False:
            if self.clients[size].cpf == cpf:
                result = True

            size -= 1

        return result

    @staticmethod
    def get_account_type():
        account_type = None
        while account_type == None:
            user_input = input(
                "Digite o tipo da conta (1 - Conta Corrente 2 - Conta Poupança): "
            )

            if user_input == "1" or user_input == "2":
                account_type = int(user_input)

        return account_type

    def get_client_index_by_cpf(self, cpf):
        result = None

        size = len(self.clients) - 1
        while size >= 0 and result == None:
            if self.clients[size].cpf == cpf:
                result = size

            size -= 1

        return result

    @staticmethod
    def float_input(message="\nDigite um valor: "):
        float_input = None
        while float_input == None:

            try:
                number = float(input(message))

                float_input = number
            except Exception as e:
                print("\nvalor invalido!\n")

        return float_input

    def register_client(self):
        name = input("Digite o seu nome: ")
        cpf = input("Digite seu CPF: ")

        if self.cpf_already_exists(cpf):
            print("\nCPF já existe!\n")

        else:
            self.clients.append(Client(name, cpf))
            print("\nCliente criado com sucesso!\n")

    def create_current_account(self):
        cpf = input("Digite seu CPF: ")

        print(self.cpf_already_exists(cpf))
        if self.cpf_already_exists(cpf):
            index = self.get_client_index_by_cpf(cpf)
            if self.clients[index].current_account != None:
                print("\nVocê já possui uma conta corrente!\n")
            else:
                account_number = Bank.generate_account_number()
                self.clients[index].current_account = CurrentAccount(
                    account_number, 0, History()
                )

                Bank.increment_total_account()
                print("\nConta criada com sucesso!\n")

        else:
            print("\nEste CPF não existe!\n")

    def create_savings_account(self):
        cpf = input("Digite seu CPF: ")

        if self.cpf_already_exists(cpf):
            index = self.get_client_index_by_cpf(cpf)
            if self.clients[index].savings_account != None:
                print("\nVocê já possui uma conta poupança\n")
            else:
                account_number = Bank.generate_account_number()
                self.clients[index].savings_account = SavingsAccount(
                    account_number, 0, History()
                )

                Bank.increment_total_account()
                print("\nConta criada com sucesso!\n")

        else:
            print("\nEste CPF não existe!\n")

    def create_life_insurance(self):
        cpf = input("Digite seu CPF: ")

        value = Bank.float_input("Digite o valor total do seguro: ")
        index = self.get_client_index_by_cpf(cpf)

        if self.cpf_already_exists(cpf):
            self.clients[index].life_insurance.append(LifeInsurance(value))

        else:
            print("\nEste CPF não existe!\n")

    def calculate_taxation(self):
        taxation = float(0)

        for client in self.clients:
            if client.current_account != None:
                taxation += client.current_account.calculate_taxation()

            for life_insurance in client.life_insurance:
                taxation += life_insurance.calculate_taxation()

        Bank.taxations.append(taxation)

        for index, t in enumerate(Bank.taxations):
            print(f"{index + 1} tributação = {t:.2f}")

    def draw(self):
        cpf = input("Digite o CPF da conta que deseja sacar: ")
        account_type = Bank.get_account_type()
        value = Bank.float_input()

        if self.cpf_already_exists(cpf):

            index = self.get_client_index_by_cpf(cpf)

            if account_type == 1 and self.clients[index].current_account != None:
                try:

                    self.clients[index].current_account.draw(value)
                    print("\nSaque realizado com sucesso!\n")
                except Exception as e:
                    print(e)

            elif account_type == 2 and self.clients[index].savings_account != None:
                try:
                    self.clients[index].savings_account.draw(value)
                    print("\nSaque realizado com sucesso!\n")
                except Exception as e:
                    print(e)

            else:
                print(f"\nO usuario de CPF {cpf} não tem uma conta do tipo digitado\n")

        else:
            print("\nEste CPF não existe!\n")

    def deposit(self):
        cpf = input("Digite o CPF da conta que deseja depositar: ")
        account_type = Bank.get_account_type()
        value = Bank.float_input()

        if self.cpf_already_exists(cpf):

            index = self.get_client_index_by_cpf(cpf)

            if account_type == 1 and self.clients[index].current_account != None:
                try:

                    self.clients[index].current_account.deposit(value)
                    print("\nDeposito realizado com sucesso!\n")

                except Exception as e:
                    print(e)

            elif account_type == 2 and self.clients[index].savings_account != None:
                try:
                    self.clients[index].savings_account.deposit(value)
                    print("\nDeposito realizado com sucesso!\n")
                except Exception as e:
                    print(e)

            else:
                print(f"\nO usuario de CPF {cpf} não tem uma conta do tipo digitado\n")

        else:
            print("\nEste CPF não existe!\n")

    def transfer(self):

        cpf = input("Digite o CPF da conta que deseja depositar: ")
        cpf_destiny = input("Digite o CPF da conta destino : ")

        account_type = Bank.get_account_type()

        value = Bank.float_input()

        if self.cpf_already_exists(cpf) and self.cpf_already_exists(cpf_destiny):

            index = self.get_client_index_by_cpf(cpf)
            index_destiny = self.get_client_index_by_cpf(cpf_destiny)

            if (
                account_type == 1
                and self.clients[index].current_account != None
                and self.clients[index_destiny].current_account != None
            ):
                try:

                    self.clients[index].current_account.transfer(
                        value, self.clients[index_destiny].current_account
                    )
                    print("\nTransfêrencia realizada com sucesso!\n")

                except Exception as e:
                    print(e)

            elif (
                account_type == 2
                and self.clients[index].savings_account != None
                and self.clients[index_destiny].savings_account != None
            ):
                try:
                    self.clients[index].savings_account.transfer(
                        value, self.clients[index_destiny].savings_account
                    )
                    print("\nTransfêrencia realizada com sucesso!\n")
                except Exception as e:
                    print(e)

            else:
                print(f"\nO usuario de CPF {cpf} não tem uma conta do tipo digitado\n")

        else:
            print("\nEste CPF não existe!\n")

    def print_history_account(self):
        cpf = input("Digite o CPF da conta que deseja visualizar o historico: ")
        account_type = Bank.get_account_type()

        if self.cpf_already_exists(cpf):

            index = self.get_client_index_by_cpf(cpf)

            if account_type == 1 and self.clients[index].current_account != None:
                try:
                    print(
                        f"\nsaldo da conta corrente: {self.clients[index].current_account.balance}\n"
                    )
                    print(self.clients[index].current_account.history.get_history())

                except Exception as e:
                    print(e)

            elif account_type == 2 and self.clients[index].savings_account != None:
                try:
                    print(
                        f"\nsaldo da conta poupança: {self.clients[index].savings_account.balance}\n"
                    )
                    print(self.clients[index].savings_account.history.get_history())

                except Exception as e:
                    print(e)

            else:
                print(f"\nO usuario de CPF {cpf} não tem uma conta do tipo digitado\n")

        else:
            print("\nEste CPF não existe!\n")

    def display_information_bank(self):

        print(f"\nO banco possui {Bank.total_accounts} contas\n")

        for client in self.clients:
            print("=" * 50)
            print(f"\nCliente: {client.name}")

            if client.current_account != None:
                print("Possui conta corrente.")

            if client.savings_account != None:
                print("Possui conta poupança.")

            print(f"Possui {len(client.life_insurance)} seguros de vida\n")

    def menu_options(self):
        print(
            "1 - Criar cliente\n2 - Criar conta corrente\n3 - Criar conta poupança\n4 - Criar seguro de vida\n5 - Sacar\n6 - Depositar\n7 - Transferir\n8 - Imprimir historico da conta\n9 - Tributação\n10 - imprimir informações do banco\n"
        )

        options = int(input("Digite uma opção: "))
        return options

    def menu(self):
        while True:
            options = self.menu_options()

            if options == 1:
                self.register_client()

            elif options == 2:
                self.create_current_account()

            elif options == 3:
                self.create_savings_account()

            elif options == 4:
                self.create_life_insurance()

            elif options == 5:
                self.draw()

            elif options == 6:
                self.deposit()

            elif options == 7:
                self.transfer()

            elif options == 8:
                self.print_history_account()

            elif options == 9:
                self.calculate_taxation()

            elif options == 10:
                self.display_information_bank()
