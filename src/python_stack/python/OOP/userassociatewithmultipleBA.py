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
        self.accounts = []
    def make_accounts(self,num):
        for i in range(0,num,1):
            self.accounts.append(BankAccount(0.02,0))
    def make_withdraw(self,amount,num):
        self.accounts[num].withdraw(amount)
        return self
    def make_deposit(self,amount,num):
        self.accounts[num].deposit(amount)
        return self
    def display_account_balance(self,num):
        self.accounts[num].display_account_info()
        return self
    def transfer_money(self,num,other,num2,amount):
        self.accounts[num].balance = self.accounts[num].balance - amount
        other.accounts[num2].balance = other.accounts[num2].balance + amount
        return self
    def test_method(self,num):
        self.accounts[num].deposit(100)		# we can call the BankAccount instance's methods
        print(self.accounts[num].balance)

jack = user("Jack")
jill = user("Jill")
jack.make_accounts(2)
jill.make_accounts(1)

jack.make_deposit(100,0).display_account_balance(0).make_deposit(200,1).display_account_balance(1).transfer_money(0,jill,0,100).display_account_balance(0)
jill.display_account_balance(0)


# jack = user("Jack")
# jack.make_deposit(200).display_user_balance().make_withdraw(100).display_user_balance()


# jill= user("jill")
# jack.transfer_money(jill,100)

# jack.display_user_balance()
# jill.display_user_balance()




