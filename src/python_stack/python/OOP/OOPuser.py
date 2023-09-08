class user:
    def __init__(self,name):
        self.name = name
        self.balance = 0
    def make_withdraw(self,amount):
        self.balance = self.balance - amount
    def make_deposit(self,amount):
        self.balance = self.balance + amount
    def display_user_balance(self):
        print("{} = {}".format(self.name,self.balance))
    def transfer_money(self,other,amount):
        self.balance = self.balance - amount
        other.balance = other.balance + amount

jack = user("jack")
jill = user("jill")
jon = user("jon")

jack.make_deposit(33)
jack.make_deposit(33)
jack.make_deposit(33)
jack.make_withdraw(49)
jack.display_user_balance()

jill.make_deposit(100)
jill.make_deposit(100)
jill.make_withdraw(50)
jill.make_withdraw(50)
jill.display_user_balance()

jon.make_deposit(500)
jon.make_withdraw(100)
jon.make_withdraw(100)
jon.make_withdraw(100)
jon.display_user_balance()

print("\nJack transfer to jon\n")
jack.transfer_money(jon,50)

jack.display_user_balance()
jill.display_user_balance()
jon.display_user_balance()
