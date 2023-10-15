import random
import time
def CountingSort(input):
    size  = len(input)
    max_value = max(input)
    min_value = min(input)

    # Initializing the count array. Its size will be = to (max value - min value + 1)  of original array
    count = [0] * (max_value - min_value + 1)
    output = [0] * size

    # Store the count of each element in count array

    for i in range(0, size): 
        count[input[i] - min_value] += 1  

# input[i] is the current element in the input array.
# min_value is the smallest element in the input array.
# input[i] - min_value gives an index relative to the smallest element.
# For example, if min_value is 1, and the current element is 3, then input[i] - min_value is 2. This means that we are counting the number of occurrences of element 3 in the input array. We then increment the count at that index by 1.

# So, this line essentially counts the occurrences of each element in the input array and stores it in the corresponding position in the count array. This is a crucial step in the Counting Sort algorithm, as it helps in determining the correct position of each element in the sorted output.


    # For Storing the cumulative count
    for i in range(1, max_value - min_value + 1):
        count[i] += count[i-1]

    # for getting the output array
    i = size - 1
    while i >= 0:
        output[count[input[i] - min_value] - 1] = input[i]
        count[input[i] - min_value] -= 1
        i -= 1


#         The loop starts by initializing i to the index of the last element in the input array (size - 1).
# It continues until i reaches 0.
# Inside the loop, the following steps are performed:
# count[input[i] - min_value] calculates the position where the current element input[i] should be placed in the output array. This is possible because we previously calculated cumulative counts.
# output[count[input[i] - min_value] - 1] = input[i] places the element at the calculated position in the output array.
# count[input[i] - min_value] -= 1 decrements the count of the element in the count array. This is important because if there are duplicate elements, we want the next occurrence to be placed at the correct position.
# i -= 1 moves to the next element in the input array.
# This loop effectively arranges the elements in the output array according to their correct positions determined by the cumulative count.

# After this loop, the output array contains the sorted elements, and it will be copied back to the original input array in the final step


  
    # Copy the sorted elements back into original array
    for i in range(0, size):
        input[i] = output[i]

    return input


def generate_random_array(size, min_value, max_value):
 
    return [random.randint(min_value, max_value) for _ in range(size)]


####### INput ############
array = generate_random_array(1000000, 1, 100000000)
array = [-5, -10, 0, -3, 8, 5, -1, 10] 

start = time.time()
N_array = CountingSort(array)
end = time.time()
TotalTime = end-start
print(N_array)
print("THe Time to sort the Array :",TotalTime)
