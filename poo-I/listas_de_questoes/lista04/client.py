class Client:
    def __init__(self, name, cpf) -> None:
        self._name = name
        self._cpf = cpf
        self._current_account = None
        self._savings_account = None
        self._life_insurance = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, value):
        self._cpf = value

    @property
    def current_account(self):
        return self._current_account

    @current_account.setter
    def current_account(self, value):
        self._current_account = value

    @property
    def savings_account(self):
        return self._savings_account

    @savings_account.setter
    def savings_account(self, value):
        self._savings_account = value

    @property
    def life_insurance(self):
        return self._life_insurance

    @life_insurance.setter
    def life_insurance(self, value):
        self._life_insurance = value
