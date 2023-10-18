import random
import time
def CountingSort(input):
    size  = len(input)
    max_value = max(input)
    min_value = min(input)

    # Initializing the count array. Its size will be = to (max value - min value + 1)  of original array
    count = [0] * (max_value - min_value + 1)
    #output array size = input array
    output = [0] * size

    # Storing the count of each element in count array
    for i in range(0, size): 
        count[input[i] - min_value] += 1  
    

    # For String the cumulative count
    for i in range(1, max_value - min_value + 1):
        count[i] += count[i-1]
    

    # for geTting the output array
    i = size - 1
    while i >= 0:
        output[count[input[i] - min_value] - 1] = input[i]
        count[input[i] - min_value] -= 1
        i -= 1
        
    return output

   


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
