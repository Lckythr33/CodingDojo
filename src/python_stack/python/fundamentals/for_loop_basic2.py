def biggieSize(list):
    for i in range(0,len(list),1):
         if(list[i]>0):
             list[i]="big"
    return list
testRet = biggieSize([-1, 3, 5, -5])
print(testRet)

def countPos(list):
    c=0
    for i in range(0,len(list),1):
        if(list[i]>0):
            c += 1
    list[len(list)-1]=c
    return list
testRet=countPos([-1,1,1,1])
print(testRet)
testRet=countPos([1,6,-4,-2,-7,-2])
print(testRet)

def sumTots(list):
    sum=0
    for i in range(0,len(list),1):
        sum += list[i]
    return sum
testRet=sumTots([1,2,3,4])
print(testRet)
testRet=sumTots([6,3,-2])
print(testRet)

def avg(list):
    sum=0
    for i in range(0,len(list),1):
        sum += list[i]
    return sum/len(list)
testRet=avg([1,2,3,4])
print(testRet)

def findLen(list):
    length = 0
    for i in range(0,len(list),1):
        length += 1
    return length
testRet=findLen([37,2,1,-9])
print(testRet)

def findMin(list):
    if(len(list)<1):
       return "false"
    else:
        min = list[0]
        for i in range(1,len(list),1):
            if(min > list[i]):
                min = list[i]
        return min
testRet=findMin([37,2,1,-9])
print(testRet)
testRet=findMin([])
print(testRet)

def findMax(list):
    if(len(list)<1):
       return "false"
    else:
        max = list[0]
        for i in range(1,len(list),1):
            if(max < list[i]):
                max = list[i]
        return max
testRet=findMax([37,2,1,-9])
print(testRet)
testRet=findMax([])
print(testRet)






