import random
import time

def RandomArray(size):
    return [random.randint(0, 20) for _ in range(size)]

def MergeSort(arr, start, end):
    if start < end:

        mid = (start + end) // 2

        print("start Value : ",start)
        print("end Value : ",end)
        print("Mid Value : ",mid)
        
        Merge(arr, start, mid, end)
                     0     2    5
def Merge(arr, p, q, r):
    left = arr[p:q+1]   0 : 2
    right = arr[q+1:r+1]   3 : 5

    i = j = 0
    k = p

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

array = RandomArray(8)
array = [6,5,4,3,2,1]
start_time = time.time()
MergeSort(array, 0, len(array)-1)
end_time = time.time()

RUNTIME = end_time - start_time
print("array sorted = ",array)
print("TOTAL RUNTIME =  ",RUNTIME)

