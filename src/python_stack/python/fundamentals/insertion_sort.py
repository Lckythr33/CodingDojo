# Python Insertion Sort 
  
# Function to do insertion sort 
def insertionSort(myList): 
  
    # Traverse through 1 to len(myList) 
    for i in range(1, len(myList)): 
  
        curr = myList[i] 
  
        # Move elements of myList[0..i-1], that are 
        # greater than curr, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and curr < myList[j] : 
                myList[j+1] = myList[j] 
                j -= 1
        myList[j+1] = curr 

    return myList
  
test = insertionSort([12, 11, 13, 5, 6]) 
print(test)