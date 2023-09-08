class product:
    def __init__(self,id=0, name="", price=0, cat=""):
        self.name = name
        self.price = price
        self.category = cat
        self.id = id
    def update_price(self,newPrice):
        self.price = newPrice
        return self
    def print_info(self):
        print("{}, {}, {},".format(self.name,self.price,self.category))
        return self
    