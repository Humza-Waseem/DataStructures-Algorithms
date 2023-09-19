import random
import time

def RandomArray(size):
    return [random.randint(0, 100000) for _ in range(size)]

def MergeSort(arr, start, end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(arr, start, mid)
        MergeSort(arr, mid + 1, end)
        Merge(arr, start, mid, end)

def Merge(arr, p, q, r):
    left = arr[p:q+1]
    right = arr[q+1:r+1]

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

array = RandomArray(100)

start_time = time.time()
MergeSort(array, 0, len(array)-1)
end_time = time.time()

RUNTIME = end_time - start_time
print("array sorted = ",array)
print("TOTAL RUNTIME =  ",RUNTIME)

