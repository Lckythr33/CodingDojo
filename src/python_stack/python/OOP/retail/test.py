from store import store
from product import product 

fruitStand = store("fruitStand")
apple = product("apple",2,"fruit")
ban = product("bannana",2,"fruit")

fruitStand.add_Products(apple)
fruitStand.add_Products(ban)

fruitStand.diplay_Products()


