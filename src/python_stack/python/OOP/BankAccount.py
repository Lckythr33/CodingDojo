class bankaccount:
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
ac1 = bankaccount(.03)
ac2 = bankaccount(.08,0)
ac1.deposit(33).deposit(33).deposit(33).withdraw(49).yield_interest().display_account_info()
print("\n")
ac2.deposit(500).deposit(500).withdraw(25).withdraw(25).withdraw(25).withdraw(25).yield_interest().display_account_info()


