# import random
# import time

# def generate_random_array(size, min_value, max_value):

#     return [random.randint(min_value, max_value) for _ in range(size)]


# def RadixSort(array):
#     max_value = max(array) # to find the max value of the array
#     min_value = min(array) # to find the max value of the array


#     #to find the length of the maximum number in the array
#     max_valueNumers = str(max_value)
#     max_valueNumers = len(max_valueNumers)
#     for i in range(len(array)):
#         # if array[i]<0:
#         #    array[i] = str(array[i])
#         #    array[i] =


#         # else:
#         length  = str(array)
#         length = len(array[i])
#         if( length < 4):
#            array[i] = str(array[i])
#            array[i] = '0' + array[i]
#         else:

#             continue

#     def CountingSort(input):
#      size  = len(input)
#      max_value = max(input)
#      min_value = min(input)

#     # Initializing the count array
#     buckets = [0] * max_valueNumers

#     # Store the count of each element in count array
#     for i in range(0, size):
#         count[input[i] - min_value] += 1


#     # Store the cumulative count
#     for i in range(1, max_value - min_value + 1):
#         count[i] += count[i-1]

#     output = [0] * size

#     i = size - 1
#     while i >= 0:
#         output[count[input[i] - min_value] - 1] = input[i]
#         count[input[i] - min_value] -= 1
#         i -= 1


#     # Copy the sorted elements back into original array
#     for i in range(0, size):
#         input[i] = output[i]

#     return input
# array = generate_random_array(1000000, 1, 100000000)
# array = [-5, -10, 0, -3, 8, 5, -1, 1000]
# array = [3,5,74,232,34,644]
# start = time.time()
# N_array = RadixSort(array)
# end = time.time()
# TotalTime = end-start
# print(N_array)
# print("THe Time to sort the Array :",TotalTime)

