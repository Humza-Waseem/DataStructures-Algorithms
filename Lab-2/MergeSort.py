import random
import time

def RandomArray(size):
    return [random.randint(0, 20) for _ in range(size)]

# def MergeSort(arr, start, end):
#     if start < end:

#         mid = (start + end) // 2

#         print("start Value : ",start)
#         print("end Value : ",end)
#         print("Mid Value : ",mid)
        
#         Merge(arr, start, mid, end)
#                   #  0     2    5
# def Merge(arr, start, mid, end):
#     left = arr[start:mid+1]   #0 : 2
#     right = arr[mid+1:end+1]   #3 : 5

#     i = j = 0
#     k = p

#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             arr[k] = left[i]
#             i += 1
#         else:
#             arr[k] = right[j]
#             j += 1
#         k += 1

#     while i < len(left):
#         arr[k] = left[i]
#         i += 1
#         k += 1

#     while j < len(right):
#         arr[k] = right[j]
#         j += 1
#         k += 1
def merge_sort(arr):
    if len(arr) <= 1:  # Base case: If the list has 0 or 1 elements, it is already sorted.
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort each half
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves back together
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    # Compare elements from both lists and append the smaller one to the result
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append any remaining elements from the left and right lists (if any)
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# array = RandomArray(8)

array = [6,5,4,3,2,1]

start_time = time.time()
array = merge_sort(array)
end_time = time.time()


RUNTIME = end_time - start_time

print("array sorted = ",array)
print("TOTAL RUNTIME =  ",RUNTIME)

