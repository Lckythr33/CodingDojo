for i in range(0,151,1):
   print(i)

for i in range(5,1005,5):
   print(i)

for i in range(1,101,1):
    if(i % 10 == 0):
        print("Coding Dojo")
    elif(i % 5 == 0):
        print("Coding")

sum=0;
for i in range(0,500001,1):
    if(i % 2 == 1):
        sum += i;
        print(sum)

for i in range(2018,-4,-4):
    if(i>0):
        print(i)
    else:
        print(0)

lowNum = 2
highNum = 9
mult = 3
for lowNum in range(lowNum,highNum+1,1):
    if(lowNum % mult == 0):
     print(lowNum)



