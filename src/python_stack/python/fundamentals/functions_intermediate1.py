import random
def randInt(min=0 , max=0):
    if(min>max and max != 0 or max <0):
        return -1;
    else:
        if(min==0 and max==0):
            num = random.randint(0,100)
            return num
            
        elif(min == 0 and max != 0):
            return random.randint(0,max)
            
        elif(max == 0 and min != 0):
            return random.randint(min,100)
            
        else:
            return random.randint(min,max)
        

print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500