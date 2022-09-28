


class User:
    def __init__(self, name , email):
        self.first = name
        self.email = email
        self.account = BankAccount(0.02, 0)

    def display_info(self,name):
        print(self.name)

    def make_depoist(self):
        self.account.deposit(400)
        return self

    def make_withdrawal(self):
        self.account.withdraw(200)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

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



# checkings = User("Mykael Sicard" , "mykaels@gmail.com" )
# checkings.make_depoist().make_withdrawal().display_user_balance()
# savings = User()
