def countdown(x):
    for i in range(x,-1,-1):
        print(i)
countdown(100)

def printReturn(list):
    print(list[0])
    return list[1]
testRet = printReturn([30,25])
print("returned:",testRet)

def firstPlusLen(x,list):
    add = x + len(list)
    return add
testRet = firstPlusLen(5,[1,2,3,4,5,6,7,8,9,10])
print(testRet)

def valsGreaterThanSecond(list):
    c = 0
    newList= []
    for i in range(0,len(list),1):
        if(list[i] > list[1]):
            c += 1
            newList.append(list[i])
    print("number of elements greater than second val =",c)
    return newList          
testRet = valsGreaterThanSecond([5,2,3,2,1,4])
print(testRet)

def createList(size,val):
    list = []
    for i in range(0,size,1):
        list.append(val)
    return list
testRet = createList(6,2)
print(testRet)