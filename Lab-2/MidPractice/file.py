# def BubbleSort(array,start,end):
#     for i in range(start + 1,end):
#         for  j in range( start,end - i):
#             if(array[j] > array[i]):
#                  array[j],array[j+1] = array[j+1],array[j]
#     return array


# def SelectionSort(arr,start,end):
#     for i in range(start,end-1):
#         min = arr[i]
#         for j in range(i+1 ,end):
#             if (min > array[j]):
                
#                 temp = arr[j]
#                 arr[j] = min
#                 arr[i] = temp
#             print( arr)
#     return arr


#     return array
def SelectionSort(array,start, end): 
    for i in range(end):
        min = array[i]
        for j in range(i + 1, end):
            if(array[j]  < min):
                min = array[j]
                
        # array[i],min = min, array[i]
        temp = array[i]
        arr[i] = min
        min = temp
        
                # array[j],array[i] = min,array[j]
    return array
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage
my_list = [64, 34, 25, 12, 22, 11, 90]

print("Original List:", my_list)
selection_sort(my_list)
print("Sorted List:", my_list)



#  for i in range(0,len(array)-1 , 1):
#     print("Step : ",i+1)
#     print("________________________")
#     minimum = array[i]
#     print("Minimum value at step :",i + 1," is ",minimum)
#     for j in range(i +1,len(array),1):
#         if minimum > array[j]:
#             minimum = array[j]    #   array [i+1]  = minimum that is array[i]   in the first case i = 0
            
#             # swap
#             temp = array[i]
#             array[i] = minimum
#             array[j] = temp
#         print("array at Step : ",i+1, " is ",array)
#         print("________________________")
#         print("")    







array = [3,2,1]
n = len(array) 
NewArray =  SelectionSort(array,0,n)
print(NewArray)

