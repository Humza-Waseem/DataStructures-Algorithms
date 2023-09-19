#  Input From User
# a=input("Enter any number:")
# b= int(a)
# print("the entered number is :",a)

  

  # >>>>>>>>  Array declarations


# student_names = ['hamza','abdullah','farjad']

# student_marks = [40, 20, 80]
# print( " {0} has obtained {1} " + student_names[0] ,student_marks[0])

# Array_student_2D = [["hamza","farjad","mehar","bilal"],[2,1,3,4]]
# print("Array is : ",Array_student_2D)




#     ARRAY OF ZEROS

# array =[0 *10]
# print(array)


# THis will make a 2D array of 3*4 having 3Rows and 4Columns
# array1 = [[0 for x in range(4)] for y in range(3)]
# print(array1)




# 1D array of Random ints
# import random
# array = []
# min = 0
# max = 50
# n = 5
# # Iterate the LOOP from 0 to "n" numbers
# for i in range( 0 , n):   
#     num = random.randint(min,max)
#     array.append(num)
#     print(num)



# str = ["university","of Engineering","&","technology"]
# # print(len(str))
# # # for x in range(len(str)):
# # #         print(str[x])

# # for x in str:

# str.reverse()
# print(str)




# Example 1.7: Slicing of Arrays—Extracting subarrays
# arr = ['a', 'b','c' ,'d']
#       # 0    1   2    3 
#       #    
# # prints the elements of an array from 1 index to 3 (3 is not included?\)
# print(arr[1:3])




# arr = [[1 , 2, 3, 4, 5],
# [2 , 20, 928, 19, 0]]
#     #  0,  1, 2, 3, 4
#     # -5, -4, -3,-2,-1
# print("The last two element are",arr [-3:-1] )


# arr=["hamza","farjad","mehar","bilal"]
# n = 0

# for x in arr:
#     # print(arr[n])
#     if(arr[n] == "mehar"):
#         print("mehar found at ",n)
#         break
#     else:
#          n+=1
# print(arr)



#  PRinting the array in the increasing order of indeces
# string = ["U","E","T"]
# for x in range(len(string)):
#   print(string[x])
#   x+=1  



#  PRinting the array in the reverse order of indeces
# string = ["U","E","T"]
# for x in range(len(string)):
#   string.reverse()
#   print(string[x])
#   x+=1  


# >>>>>>>>>>>>>>    Read data from File

# MyFile = open ( file = 'text.txt', mode = 'r' )    #open the file in read mode
# lines = MyFile.read()                        # READ the line from myFile
# numbers = [1,2,3,4,5]          # Here we have created a new array of name numbers 
# arr = lines.split()             # Here we are spliting LINES that we have already read from the file
# for s in arr:                     # For Loop  checks s in "arr" named array .. 's' is the index
#    num = int(s)            # for first iteration make the first index of arr equal to "num" and so on....
#    numbers.append(num)   # append the num[s]  to the "numbers" array

# print(numbers)               # after appending the "numbers"  array print the array



# >>>>>>>>>>>>>>    Write data to File

# student_names = ["hamza","kamran","ali"]
# f = open (file = "text.txt" , mode = "w")
# for names in student_names:
#      f.write (names + "\n")



#  Play with functions


# def printArray(arr):
#   for names in arr:
#     print(names )

# student_names = ["hamza","kamran","ali","mehar"] #declaring the array and then passing it to the function "printArray"
# printArray(student_names)

# def funcReturn ():
#    student_names = ["hamza","kamran","ali","mehar"]
#    return student_names

# NewArray = funcReturn()

# print(NewArray)

# array = ["U","E" ,"T"]
# # print(len(array))
# # range is set to arrayLength-1, to -1 and decrement is -1
# for i in range(len(array) -1,-1,-1):
#   print(array[i])
  
  


  # iterative method for printing integers in increasing order

# num = 0
# while(num >= 0):
#   print(num)
#   num = num +1



# arr = [1,2,4,4,4,9,7,8,9,10]
# for i in arr:
#  print(i)
# #  i= i+1




# def addArray(array):
#    for i in range(  0 ,len(array), 1 ):
#     print(array[i])
    
# array = ["hamza", "bilal","dado","mama","dad"]
# addArray(array)

# sum = 0 
# for i in range (11):
#   sum += i
# print(sum)


# array = ["hamza", "bilal","dado","mama","dad"]


# def printArray(array):
#    i= i+ 1
#    print(array[i])
#    printArray(array)


# printing the sum of  first 10 natural  numbers

# sum = 0
# for i in range(11):
#   sum+=i
#   print(sum)


# printing array through recursion

# def printArray(arr, i):
#   if(i>=len(arr)):
#     return None
#   else:  
#     print(arr[i])
#     i=i+1
#     printArray(arr,i)

# array = [1,2,3,4,5,6,7,8,9,10]
# i= 0
# printArray(array,i)


# print Power

# num = 2
# power = 7
# sum = 1

# for i in range (power):
#    sum = sum *num
# print(sum)
 
######################################   Problem 1   #########################################
 
# def SearchA(arr , x):
#   for i in range(len(arr)-1):
#     if(arr[i] <arr[x]):
#       continue

#     elif(arr[i]  == arr[x]):
#       return arr[x],arr[x+1]
#   return none 

# array = [22,2,1,7,11,13,5,2,9]
# x = input("Enter the element to be searched")
# x = int(x)
# NewArray = SearchA(array, x) 
# print("Index Is :",NewArray)

######################################   Problem 2    #########################################

# def Minimun(Arr, startingIndex , endingIndex):
#   index = 0
#   for i in range(startingIndex,endingIndex,1):
#     index = Arr[i]

#     if(Arr[i+1] < index):
#       # index = Arr[i]
#       index = Arr[i+1]
      

#   return index


# array = [3,4,7,8,0,1,23,-2,-5]
# startingIndex = int(input("Enter Starting Index"))
# endingIndex = int(input("Enter ending Index"))
# index = Minimun(array,startingIndex, endingIndex)
# print("The Minimum value is at index : ",index)

######################################   Problem 3    #########################################

# def Sort4(array):
#   lowestIndex = 0
#   for i in array:
#     if(array!= None):
      
#       lowestIndex = array[i]
#       if(array[i+1] < array[i]):
#         lowestIndex= array[i + 1]
       
#         # array[i] = lowestIndex
    
#       return lowestIndex    
#     elif(array== None):
#       return None

#   return None


# array = [3,4,7,8,0,1,23,-2,-5]
# ar = Sort4(array)
# print("lowest index is :" ,ar)



######################################   Problem 6    #########################################

# def SumIterative(numbers):
#   sum_Of_digits = 0
#   while(numbers >0):
#     num = (numbers % 10)
#     sum_Of_digits = sum_Of_digits + num
#     num = numbers - num
    
#   return sum_Of_digits
   
# # 
# digits = int(input("ENter the digits : "))
# sum = SumIterative(digits)
# print("The summation is ",sum)


######################################   Problem 4    #########################################
# array = [3,4,7,8,0,1,23,-2,-5]
# arrayN = sorted(array)
# print('Sorted Array:', arrayN)


# array = [4,2,9,6,3]
# firstIndex = 0

# for i in range(len(array)-1):
#    Minimum_index = array[i]

#    if(Minimum_index > array[i+1]):

#        temp  =array[i]
#        array[i] = array[i+1]
#        array[i+1] = temp     
# print("final array is : " ,array)  


######################################   Problem 5    #########################################

# s = "University of Engineering and Technology Lahore"
# n = s[27:40]
# print(n[-1::-1])

# def RowWiseSum(A):
#   sumation = 0
#   for i in range(0,len(A),1):
#     for  j in range(0,len(A),1):
#       sumation =  sumation + A[j]
#     print(sumation)  
     

# A = [[1,13,13],[5,11,6],[4,4,9]]



# RowWiseSum(A)

# def ColumnWiseSum(A):
#  for i in range(0,len(A),1):
#    for  j in range(i,len(A),1):
     



     
# s= "radar"
 
# i = 0 
# while(len(s) > 0):
#   if(s[i] == s[-i]):
#     print(s[i])
#     i+=1

# print("palindrome")
 

