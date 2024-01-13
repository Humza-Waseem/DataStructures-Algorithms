# odd indexes
def quicksort(arr, start, end):
    if start < end:
        boundary = start - 1
        pivot = arr[end]
        for j in range(start, end):
            if j % 2 == 0:
                if arr[j] <= pivot:
                    boundary = boundary + 2
                    arr[j], arr[boundary] = arr[boundary], arr[j]
        arr[boundary + 1], arr[end] = arr[end], arr[boundary + 1]
        quicksort(arr, start, boundary - 1)
        quicksort(arr, boundary + 2, end)


arr = [3, 7, 1, 8, 6, 4, 5, 2]
quicksort(arr, 0, len(arr) - 1)
print(arr)



# even indexes
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort(arr, low, pivot - 1)
        quicksort(arr, pivot + 1, high)


def sort_even_indices(arr):
    even_elements = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    quicksort(even_elements, 0, len(even_elements) - 1)
    j = 0
    for i in range(len(arr)):
        if i % 2 == 0:
            arr[i] = even_elements[j]
            j += 1
    return arr


# Example usage
arr = [3, 1, 5, 8, 6, 4, 2, 7]
print(sort_even_indices(arr))
