class BankAccount:
    def __init__(self, init_rate=.01, balance=0):
        self.balance = balance
        self.iR = init_rate
    def withdraw(self,amount):
        self.balance = self.balance - amount
        return  self
    def deposit(self,amount):
        self.balance = self.balance + amount
        return  self
    def display_account_info(self):
        print("{}".format(self.balance))
        return  self
    def yield_interest(self):
        self.balance +=  (self.balance * self.iR)
        return self
class user:
    def __init__(self,name):
        self.name = name
        self.account = BankAccount(0.02,0)
    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        return self
    def make_deposit(self,amount):
        self.account.deposit(amount)
        return self
    def display_user_balance(self):
        self.account.display_account_info()
        return self
    def transfer_money(self,other,amount):
        self.account.balance = self.account.balance - amount
        other.account.balance = other.account.balance + amount
        return self
    def test_method(self):
        self.account.deposit(100)		# we can call the BankAccount instance's methods
        print(self.account.balance)
        


jack = user("Jack")
jack.make_deposit(200).display_user_balance().make_withdraw(100).display_user_balance()


jill= user("jill")
jack.transfer_money(jill,100)

jack.display_user_balance()
jill.display_user_balance()




