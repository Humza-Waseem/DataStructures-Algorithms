import time
import random

def RandomArrayGenerater(array,min,max,n):
 for i in range (0, n):
    num = random. randint (min, max)
    array. append (num)
 return array
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

def writeElementsInFile(array):
  file_name = "SortedInsertionSort.csv"
  with open(file_name, "w") as f:
    for elementOfArray in array:
      f.write(str(elementOfArray) + "\n")
  f.close()
    
array = []
min = 0
max = 30000
n = 100
array = RandomArrayGenerater(array,min,max,n)

# STARTING AND ENDING INDEX OF ARRAY
start = 0
end = len(array)-1


start_time = time.time()             # STARTING TIME OF THE PROGRAM
BubbleSort(array,start,end)          # PROGRAM FOR SORTING
end_time = time.time()               # ENDING TIME FOR THE SORTING ALGO
runtime = end_time - start_time      # CALCULATING THE RUNTIME OF THE ALGO
writeElementsInFile(array)
print("----------------------------------------------")
print("----------------------------------------------")
print("Sorted Array by Bubble Sort is : ", array)
print("----------------------------------------------")
print("----------------------------------------------")
print(f"Runtime is :",runtime," seconds When  n is :",n)





