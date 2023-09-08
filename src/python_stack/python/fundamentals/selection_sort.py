# Python Selection Sort
def selectionSort(myList):
    sortedList = []
    for i in range(len(myList)): 
            
        # Find the minimum element in myList 
        # unsorted myList
        min= i 
        for j in range(i+1, len(myList)): 
            if myList[min] > myList[j]: 
                min = j 
                
        # Swap the found minimum element with  
        # the first element         
        myList[i], myList[min] = myList[min], myList[i] 
  
    return myList
        
    
test = selectionSort([64, 25, 12, 22, 11])
print(test)
