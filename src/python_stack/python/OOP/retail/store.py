from product import product 

class store:
    def __init__(self, name):
        self.name = name
        self.productList = []
    def add_Products(self,new_product):
        self.productList.append(new_product)
    def sell_Products(self,id):
        for i in self.productList:
            if i.id == id:
                self.productList.remove(i)
    def diplay_Products(self):
         for i in range(len(self.productList)):
                print(self.productList[i].name)
    def inflation(self,percent_increase):
            for i in range(len(self.productList)):
                self.productList[i].price +=  self.productList[i].price * percent_increase 
    def set_clearance(self,category,percentage_discount):
            for i in range(len(self.productList)):
                if(self.productList[i].category == category):
                    self.productList[i].price -=  self.productList[i].price * percentage_discount 
    

