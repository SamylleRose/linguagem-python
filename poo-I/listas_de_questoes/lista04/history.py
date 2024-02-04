class History:
    def __init__(self) -> None:
        self._history = "Histórico da conta: \n"

    @property
    def history(self):
        return self._history

    @history.setter
    def history(self, value):
        self._history = value

    def get_history(self):
        return self.history

    def add_history(self, new_history):
        self.history += new_history + "\n"
