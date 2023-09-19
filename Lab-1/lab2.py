# # import numpy
# # array = []

# # start = -100
# # end = 100

# # for i in range(start,end):
# #     number = random.randint(start,end)
# #     array.append(number)
# # print(array)    


# def BubbleSort(array,start,end):


#  for j in range (0,len(array) - 1,1):
#     for i in range (0,len(array) - 1,1):
#         if(array[i] > array[i+1]):
         
#         #  swap
#            temp = array[i]
#            array[i] = array[i+1]
#            array[i+1] = temp
         
#         else:
#             continue
#  return array

# array = [9,5,8,3,1,11,10,34,9,-1,23,13]
# # array = [6,5,4,3,2,1]
# start  = array[0]
# end = len(array)
# nArray = BubbleSort(array,start,end)
# print(nArray)


 
# def factorial(n):
#  if(n==0):
#    return 1
#  else: 
#    return n* factorial(n-1)
 
# import time
# start_time = time.time()
# n = 1500
# ans= factorial(n)
# end_time = time.time()

# runtime = end_time - start_time
# print("factorial of {ans} is : " ,ans)
# print("Runtime of factorial at",n,"is",runtime,"seconds")

# def RandomArray(size):
 
#  array = ["12","23","3","2"]
  
#  f = open (file = "text.txt" , mode = "w")
#  for names in student_names:
#      f.write (names + "\n")

 
#  MyFile = open ( file = 'text.txt', mode = 'r' )
#  lines = MyFile.read()  

# RandomArray(4)


########################   Selection Sort   ############################

# array = [6,5,4,3,2,1 , 0, 9,12, 11,8,3,89,23,534,23,44,5,23,65,34,27,-1,-6,-34,-56,-4,87,-455   ]

# for i in range(0,len(array)-1 , 1):
#     minimum = array[i]
#     for j in range(i +1,len(array),1):
#         if minimum > array[j]:
#             minimum = array[j]    #   array [i+1]  = minimum that is array[i]   in the first case i = 0
            
#             # swap
#             temp = array[i]
#             array[i] = minimum
#             array[j] = temp

# print(array)              

########################   Bubble Sort   ############################

import time


# array = [6,5,4,3,2,1 ]

# array = [1, 2, 3, 4, 5, 6]
# array = [6,5,4,3,2,1 , 0, 9,12, 11,8,3,89,23,534,23,44,5,23,65,34,27,-1,-6,-34,-56,-4,87,-455   ]
# n = len(array) 
# start_time = time.time()

# for i in range(0 ,n - 1):     # number of iterations will be  (6) for array = [6,5,4,3,2,1]

#     swapped = False
#     for j in range(0 , n - 1 - i ):       # number of iterations will be (5) for array = [6,5,4,3,2,1]

#         if array[j] > array[j+1]:             

#              array[j], array[j+1] = array[j+1], array[j]      
#              swapped = True

#     if(swapped == False):
#         break
# end_time = time.time()
# runtime = end_time - start_time
# print(array)
# print("Runtime of factorial at",n,"is",runtime,"seconds")



# array = [6,5,4,3,2,1 ]
# n = len(array)
# for i in range(1,n  ):     
#     key = array[i]
    
#     for j in range(0 , n-1 ):       
#         if (key < array[j] and array[j] != 0):             
#            swap = array[j]
#            array[j]= key
#            key = swap
#            print(array)
          
         
  
# print ("Sorted Array is:",array)          #  swapped = True

def SearchA(Arr, x) :
  arrOfIndices = []
  for i in range(0,len(Arr)-1):
    if Arr[i] < Arr[x]:
      continue
      
    elif(Arr[i] == Arr[x]):
      arrOfIndices = [Arr[i],Arr[i+1]]
      return arrOfIndices
      
    



X = [22,2,1,7,11,13,5,2,9]

x = int(input("Enter the Element to search"))

temp = SearchA(X, x) 
print('The indices are',temp )



