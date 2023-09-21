import random
def writeElementsInFile(array):
  file_name = "SortedInsertionSort.csv"
  with open(file_name, "w") as f:
    for elementOfArray in array:
      f.write(str(elementOfArray) + "\n")
  f.close()

  def BubbleSort(array,start, end):
    for i in range (start , end ):                     
                                                       
        for j in range (start , end - i):
            if (array[j] > array[j + 1] ):
                                               
                       # SWAPPING
                      array[j], array[j+1] = array[j+1], array[j]      
                      swapped = True
        if(swapped == False):
           break
                
    return array
def RandomArrayGenerater(array,min,max,n):
 for i in range (0, n):
    num = random. randint (min, max)
    array. append (num)
 return array

 def InsertionSort(array,start,end):
  for i in range(start,end):
    key = array[i]                    
    j = i-1                          
    while( j>= 0 and key < array[j]):
      array[j+1] = array[j]          
      j-=1
    array[j + 1] = key       
    print("array after key replacement =  ",array)
  return array

def SelectionSort(array,start, end): 

 for i in range(0,len(array)-1 , 1):
    minimum = array[i]
    for j in range(i +1,len(array),1):
        if minimum > array[j]:
            minimum = array[j]    #   array [i+1]  = minimum that is array[i]   in the first case i = 0
            
            # swap
            temp = array[i]
            array[i] = minimum
            array[j] = temp