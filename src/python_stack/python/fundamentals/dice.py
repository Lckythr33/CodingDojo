import random
import statistics

class die:
    def __init__(self,sides=6):
        self.sides = sides
        self.rollHist = []
    def roll(self):
        self.rollHist.append(random.randint(1,self.sides))
        return self.rollHist[-1]  # -1 means return the last item.
    def rollTimes(self,times):
        for i in range(times):
            self.rollHist.append(random.randint(1,self.sides))

def rollUntilDoubles(die1,die2):
    isDoubles = False
    while(isDoubles == False):
        isDoubles = die1.roll() == die2.roll()

def getStats(die1,die2):
    
    min_num = -1
    combined_roll_values = []
    for idx in range(len(die1.rollHist)):
        combined_roll_values.append(die1.rollHist[idx] + die2.rollHist[idx])
    
    stats = {
    "num_rolls" : len(die1.rollHist),
    "min_rolled" : min(combined_roll_values),
    "max_rolled" : max(combined_roll_values),
    "average" : float("{0:.3f}".format(statistics.mean(combined_roll_values)))
}
    
    if(stats["min_rolled"] == stats["max_rolled"]):
        print("DOUBLES FIRST TRY!!")
    
    for key, val in stats.items():
        print(key,val)
   

die1=die()
die2=die()
rollUntilDoubles(die1,die2)
print(die1.rollHist)
print(die2.rollHist)
getStats(die1,die2)
