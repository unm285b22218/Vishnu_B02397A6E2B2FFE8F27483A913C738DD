class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.____account_number = account_number
    self._account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited {}. New balance: {}".format(amount,
                                                   self.__account_balance))
    else:
      print("Invalid deposit amount.")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdrew ₹{}. New balance: ₹{} ".format(amount,
                                                     self.__account_balance))

    else:
      print("Invalid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (Account #{}): ₹{}".format(
        self._account_holder_name, self.____account_number,
        self.__account_balance))


account = BankAccount(account_number="123456789",
                      account_holder_name="Harl Prabu",
                      initial_balance=5080.8)

account.display_balance()
account.deposit(580.8)
account.withdraw(289.8)
account.withdraw(20886.8)
account.display_balance()
