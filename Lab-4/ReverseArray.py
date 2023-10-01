##################  Reverse sorting of Array  ########################

# arr = [1,2,3,4,5,6]
# n = len(arr)
# for i in range(1,n):
#     key = arr[i]
#     j = i - 1

#     while(j>=0 and key > arr[j]):
#         arr[j+1] = arr[j]              # swap to array[0+1] equal to array[0]

#         j = j - 1  
#     arr[j+1 ] = key
# print("array sorted in reverse order : ",arr)

################# Recursively Dividing the Array  ######################
import random
def RandomArray(size):
    return [random.randint(0, 200) for _ in range(size)]


def recursiveDividing(array):
        print(array)
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        
        recursiveDividing(left)
        
        recursiveDividing(right)
        





array = RandomArray(100)
recursiveDividing(array)

