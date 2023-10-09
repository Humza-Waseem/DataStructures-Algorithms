def CountingSort(input):
    size  = len(array)
    output = [0] * size

    #Initialize count array
    count = [0]* 10
     
    # store the count of each elements in count array
    for i  in range(0,size):
        count[array[i]] +=1

    # store the comulative count
    for i  in range(1,10):
        count[i]+= count[i-1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -=1
        i-=1
    #copy the sorted elements into otiginal array
    for i in range(0,size):
        array[i]= output[i]

    return output

array = [9,8,75,3,6,2,1]
New_array = CountingSort(array)
print("The sorted array by counting array is ",New_array)