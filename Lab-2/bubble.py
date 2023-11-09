import time
import random
import functions

def BubbleSort(array,start, end):
    for i in range (start , end ):                     
                                          
        for j in range (start , end - i):
            if (array[j] > array[j + 1] ):
                                               
                       # SWAPPING
                      array[j], array[j+1] = array[j+1], array[j]      
                      swapped = True
        print("array at loop iteration  : ",i+1, " is : ",array)
        if(swapped == False):
           break
                
    return array

def BubbleSort(array,start, end):
    for i in range(start,end):
        for j in range(start,end-i):
            if( array[j]>array[j+1]):
                array[j],array[j+1] = array[j+1],array[j]
    return array






    
array = []
min = 0
max = 30000
n = 100
array = functions.RandomArrayGenerater(array,min,max,n)
array= [9,8,7,6,4,3,2,1]

# STARTING AND ENDING INDEX OF ARRAY
start = 0
end = len(array)-1


start_time = time.time()             # STARTING TIME OF THE PROGRAM
newArray = BubbleSort(array,start,end)          # PROGRAM FOR SORTING
end_time = time.time()               # ENDING TIME FOR THE SORTING ALGO
runtime = end_time - start_time      # CALCULATING THE RUNTIME OF THE ALGO
functions.writeElementsInFile(array)
print("----------------------------------------------")
print("----------------------------------------------")
print("Sorted Array by Bubble Sort is : ", newArray)
print("----------------------------------------------")
print("----------------------------------------------")
print(f"Runtime is :",runtime," seconds When  n is :",n)








# def BubbleSort(array,start,end):
#     for i in range(start,end):
#         for  j in range(start,end - 1):
#             if(array[j] > array[j+1]):
#                  array[j],array[j+1] = array[j+1],array[j]
#     return array


# array = [6,8,3,6,8,3,5,7,10,324,34]
# NewArray = BubbleSort(array,0,11)
# print(NewArray)
