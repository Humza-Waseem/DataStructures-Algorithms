import random 
import time
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort(arr, threshold=10):
    if len(arr) <= threshold:
        insertion_sort(arr)
    else:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
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

def RandomArray(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Example usage
if __name__ == "__main__":
   array = RandomArray(1000000)
#    print("Original array:", array)
   start_time = time.time()
   merge_sort(array)
   end_time = time.time()
   RUNTIME = end_time - start_time
#    print("Sorted array:", array)
   print("TOTAL RUNTIME =  ",RUNTIME)

