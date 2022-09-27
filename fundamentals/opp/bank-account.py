class BankAccount:
    # don't forget to add some default values for these parameters!

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self


b1 = BankAccount(.05, 400).deposit(50).deposit(100).deposit(400).withdraw(150).yield_interest().display_account_info()

b2 = BankAccount(.03, 300).deposit(20).deposit(100).withdraw(10).withdraw(20).withdraw(10).withdraw(30).yield_interest().display_account_info()
