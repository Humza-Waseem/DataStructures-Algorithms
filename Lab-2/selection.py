import time
import random
import functions

#    FUNCTION TO GENERATE AN RANDOM ARRAY


#    SELECTION SORT ALGORITHM TO SORT THE ARRAY IN ASCENDING ORDER

def SelectionSort(array,start, end): 

 for i in range(0,len(array)-1 , 1):
    print("Step : ",i+1)
    print("________________________")
    minimum = array[i]
    print("Minimum value at step :",i + 1," is ",minimum)
    for j in range(i +1,len(array),1):
        if minimum > array[j]:
            minimum = array[j]    #   array [i+1]  = minimum that is array[i]   in the first case i = 0
            
            # swap
            temp = array[i]
            array[i] = minimum
            array[j] = temp
        print("array at Step : ",i+1, " is ",array)
        print("________________________")
        print("")    

#  For writing the elements of array in the file each element on one line

   

array = []
min = 0
max = 30000
n = 5
array = functions.RandomArrayGenerater(array,min,max,n)
array =  [7,6,5,4,3,2,1]

# STARTING AND ENDING INDEX OF ARRAY
start = 0
end = len(array)-1

start_time = time.time()             # STARTING TIME OF THE PROGRAM

SelectionSort(array,start,end)          # PROGRAM FOR SORTING

end_time = time.time()               # ENDING TIME FOR THE SORTING ALGO
runtime = end_time - start_time      # CALCULATING THE RUNTIME OF THE ALGO
functions.writeElementsInFile(array)

print("----------------------------------------------")
print("----------------------------------------------")
print("Sorted Array by Selection Sort is : ", array)

print("----------------------------------------------")
print("----------------------------------------------")
print(f"Runtime is :",runtime," seconds When  n is :",n)
