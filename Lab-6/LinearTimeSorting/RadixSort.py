def counting_sort(arr, digit):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // digit       # in the first case     index = ( arr[i] = 110)  //  1(digit)  === 110
        count[index % 10] += 1          # index % 10      110 % 10 == 0 so count[0] = count[0] + 1


    for i in range(1, 10):            # For finding the commulative sum of each element in the array
        count[i] += count[i - 1]

    i = n - 1
                                              # alternatively we can write  
                                              # for i in range(len(arr), -1,-1):
    while i >= 0:                                      # b[--count[a[i]//pos]  % 10] = A[i]
        index = arr[i] // digit
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
   
    for i in range(n):         # for copying the elemets of the array
        arr[i] = output[i]


def radix_sort(arr):
    # def RadixSort(array):
#      max_element = max(array)
#      max_element = str(max_element)
#      digits = len(max_element)
    max_value = max(arr)
    digit = 1
    while max_value // digit > 0:      #  this will iterate 3 times as the max val has 3 digits
        counting_sort(arr, digit)
        digit = digit * 10



arr = [110, 45, 65, -50, 90, -602, 24, 2, 66]
counting_sort(arr)


print(arr)

# print(610/100)
