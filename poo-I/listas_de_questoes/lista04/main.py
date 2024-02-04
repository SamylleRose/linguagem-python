# from client import Client
# from account import SavingsAccount
# from history import History

# client01 = Client(name="Rei", cpf="123")
# print(client01.name)

# from account import Account
# abstract_account = Account()
# print(abstract_account)

# current_account1 = SavingsAccount(123, 0, History())
# current_account2 = SavingsAccount(234, 0, History())

# print(current_account1.balance, current_account2.balance)

# current_account1.deposit(float(200))
# current_account1.draw(float(50))

# print(current_account1.balance, current_account2.balance)

# current_account1.transfer(float(50), current_account2)

# print(current_account1.balance, current_account2.balance)

# print(current_account1.history.get_history())
# print(current_account2.history.get_history())

from bank import Bank

bank = Bank()

# bank.register_client()
bank.menu()
