class product:
    def __init__(self, name="", price=0, cat=""):
        self.name = name
        self.price = price
        self.catagory = cat
    def update_price(self,newPrice):
        self.price = newPrice
        return self
    def print_info(self):
        print("{}, {}, {},".format(self.name,self.price,self.catagory))
        return self