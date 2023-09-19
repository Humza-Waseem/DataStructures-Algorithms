import time
import random

#    FUNCTION TO GENERATE AN RANDOM ARRAY
def RandomArrayGenerater(array,min,max,n):
 for i in range (0, n):
    num = random. randint (min, max)
    array. append (num)
 return array

#    SELECTION SORT ALGORITHM TO SORT THE ARRAY IN ASCENDING ORDER

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

#  For writing the elements of array in the file each element on one line

def writeElementsInFile(array):
  file_name = "SortedInsertionSort.csv"
  with open(file_name, "w") as f:
    for elementOfArray in array:
      f.write(str(elementOfArray) + "\n")
  f.close()

   

array = []
min = 0
max = 30000
n = 40
array = RandomArrayGenerater(array,min,max,n)

# STARTING AND ENDING INDEX OF ARRAY
start = 0
end = len(array)-1

start_time = time.time()             # STARTING TIME OF THE PROGRAM

SelectionSort(array,start,end)          # PROGRAM FOR SORTING

end_time = time.time()               # ENDING TIME FOR THE SORTING ALGO
runtime = end_time - start_time      # CALCULATING THE RUNTIME OF THE ALGO
writeElementsInFile(array)

print("----------------------------------------------")
print("----------------------------------------------")
print("Sorted Array by Selection Sort is : ", array)

print("----------------------------------------------")
print("----------------------------------------------")
print(f"Runtime is :",runtime," seconds When  n is :",n)
