import random
import time
# def RandomArrayGenerater(array,min,max,n):
#  for i in range (0, n):
#     num = random. randint (min, max)
#     array. append (num)
#  return array
#
def QuickSort(A,p,r):
    if (p < r):
       q = Partition(A,p,r)
       QuickSort(A, p,q-1)
       QuickSort(A, q+1 , r )
    return A

def Partition(A,p,r):
    x = A[r]  #pivot
    i = p-1
    for j in range(p,r):

       if  A [j] <=x:    # CHeck if this element belong on the low side

           i=i + 1
           temp = A[i]
           A[j] = A[i]
           A[i] = temp
    temp = A[i+1]
    A[i+1] = A[r]
    A[r] = temp

    return i+1   # New INdex of the Pivot
#
#
# A = []
# min = 1
# max = 100
# n = 100
# A = RandomArrayGenerater(A,min,max,n)
# p = A[1]
# r = A[(len(A)-1)]
#
# # print("Value of R is :",r)
# # print("Value of p is :",p)
# # print ("The Array is : ", A )
# ArraySorted = QuickSort(A,p,r)
# print("The Sorted Array by Quick Sort is :",ArraySorted)



# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr

#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]

#     return quick_sort(left) + middle + quick_sort(right)

def RandomArray(size):
    return [random.randint(0, 2000) for _ in range(size)]

# Example usage:

my_list = RandomArray(100)

# my_list = [3, 6, 8, 10, 1, 2, 1]
start = time.time()
p = 0
r = len(my_list)-1
sorted_list = QuickSort(my_list,p,r)
end = time.time()
finalTime = end-start

print(sorted_list)
print("Time to Sort is : ",finalTime)
