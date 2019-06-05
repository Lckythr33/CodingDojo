from store import store
from product import product 

fruitStand = store("fruitStand")
apple = product(1,"apple",200,"fruit")
ban = product(2,"bannana",32,"fruit")
pin = product(3,"pineaple",42,"fruit")

fruitStand.add_Products(apple)
fruitStand.add_Products(ban)
fruitStand.add_Products(pin)
fruitStand.diplay_Products()
print("\n")
apple.print_info()
fruitStand.inflation(.10)
apple.print_info()
fruitStand.set_clearance("fruit",.10)
apple.print_info()
print("\n")
fruitStand.sell_Products(1)
fruitStand.diplay_Products()
# fruitStand.sell_Products(2)
# fruitStand.diplay_Products()
