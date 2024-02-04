from abc import ABC, abstractmethod


class Account(ABC):

    def __init__(self, number, balance, history) -> None:
        super().__init__()
        self._number = number
        self._balance = float(balance)
        self._history = history

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        self._history = value

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def transfer(self):
        pass


class CurrentAccount(Account):
    def __init__(self, number, balance, history) -> None:
        super().__init__(number, balance, history)

    def deposit(self, value):
        if not isinstance(value, float):
            raise Exception("\nValor inválido!\n")

        if value <= 0:
            raise Exception("\nValor menor ou igual a 0!\n")

        self.balance += value
        self.history.add_history(f"\nDepositou R$ {value:.2f}\n")

    def draw(self, value):
        if not isinstance(value, float):
            raise Exception("\nValor inválido\n")

        if value <= 0:
            raise Exception("\nValor menor ou igual a 0!\n")

        if value > self.balance:
            raise Exception("\nValor maior que o saldo!\n")

        self.balance -= value
        self.history.add_history(f"\nSacou R$ {value:.2f}\n")

    def transfer(self, value, destiny_account):
        if not isinstance(value, float):
            raise Exception("\nValor inválido!\n")

        if value <= 0:
            raise Exception("\nValor menor ou igual 0!\n")

        if value > self.balance:
            raise Exception("\nValor maior que o saldo!\n")

        if not isinstance(destiny_account, Account):
            raise Exception("\nConta de destino inválida!\n")

        self.balance -= value
        destiny_account.balance += value
        self.history.add_history(
            f"Transferiu R$ {value:.2f} para a conta {destiny_account.number}"
        )

        destiny_account.history.add_history(
            f"Tranferência recebida de R$ {value:.2f} da conta {self.number}"
        )


class SavingsAccount(Account):
    def __init__(self, number, balance, history) -> None:
        super().__init__(number, balance, history)

    def deposit(self, value):
        if not isinstance(value, float):
            raise Exception("\nValor inválido!\n")

        if value <= 0:
            raise Exception("\nValor menor ou igual 0!\n")

        self.balance += value
        self.history.add_history(f"\nDepositou R$ {value:.2f}")

    def draw(self, value):
        if not isinstance(value, float):
            raise Exception("\nValor inválido!\n")

        if value <= 0:
            raise Exception("\nValor menor ou igual 0!\n")

        if value > self.balance:
            raise Exception("\nValor maior que o saldo!\n")

        self.balance -= value
        self.history.add_history(f"\nSacou R$ {value:.2f}")

    def transfer(self, value, destiny_account):
        if not isinstance(value, float):
            raise Exception("\nValor inválido!\n")

        if value <= 0:
            raise Exception("\nValor menor ou igual 0!\n")

        if value > self.balance:
            raise Exception("\nValor maior que o saldo!\n")

        if not isinstance(destiny_account, Account):
            raise Exception("\nConta de destino inválida!\n")

        self.balance -= value
        destiny_account.balance += value
        self.history.add_history(
            f"\nTransferiu R$ {value:.2f} para a conta {destiny_account.number}\n"
        )

        destiny_account.history.add_history(
            f"\nTranferência recebida de R$ {value:.2f} da conta {self.number}\n"
        )


class LifeInsurance:
    def __init__(self, monthly_value) -> None:
        self._monthly_value = monthly_value
        self.total_value = 5000

    @property
    def monthly_value(self):
        return self._monthly_value
