class store:
    def __init__(self, name):
        self.name = name
        self.productList = []
    def add_Products(self,new_product):
        self.productList.append(new_product)
    def diplay_Products(self):
         for i in range(len(self.productList)):
                print(i,self.productList[i].name)
