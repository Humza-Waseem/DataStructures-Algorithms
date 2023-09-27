import time
import random
import functions



# def InsertionSort(array,start,end):
#   for i in range(start,end):
#     key = array[i]                    
#     j = i-1                          
#     while( j>= 0 and key > array[j]):
#       array[j+1] = array[j]          
#       j-=1
#     array[j + 1] = key       
#     print("array after key replacement =  ",array)
#   return array

def InsertionSort(array,start,end):
  for i in range(1, len(array)):       # start with i = 1 to length of array 
    key = array[i]                     # set the key value to array[i= 1]

    j = i-1                          # set j to i-1 so j will be equal to j= 0
    print("----------------------------------------------")

    print("Step :",i,"when i = ",i," and j = ",j)
    print("----------------------------------------------")


    # print("value of j before while loop : ",j)
    # print("value of i before while loop : ",i)
    while j >= 0 and array[j] < key:   # while  j is greater than or equal to 0 and array[j = 0] greater than key value 
      array[j+1] = array[j]              # swap to array[0+1] equal to array[0]

      j -= 1                         # j = j-1
      print("array is before key replacement= ",array)
      print("j value after decrement is :",j)
      
    array[j+1]  = key                # array[j + 1]  set to key  this statement is outside of while loop  -1+1 = j{0}
    print("after key replacement : ",array)
    print("value of j after key replacement and while loop: ",j)
  return array




  

array = []
min = 0
max = 30
n = 10

array = functions.RandomArrayGenerater(array,min,max,n)

# STARTING AND ENDING INDEX OF array
array= [5,43,76,2,98,23,12,32]

start = 1
end = len(array) 

print("array before doing anything : ",array)
start_time = time.time()             # STARTING TIME OF THE PROGRAM
InsertionSort(array,start,end)          # PROGRAM FOR SORTING
end_time = time.time()               # ENDING TIME FOR THE SORTING ALGO
runtime = end_time - start_time      # CALCULATING THE RUNTIME OF THE ALGO

functions.writeElementsInFile(array)

print("----------------------------------------------")
print("Sorted array by Insertion Sort is : ", array)
print("----------------------------------------------")
print("----------------------------------------------")
print(f"Runtime is :",runtime," seconds When  n is :",n)
print("----------------------------------------------")







################################     STEP BY STEP EXPLANATION   #####################################


