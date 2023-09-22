import time
A= [
[1,4],    # 0
[2,5],    # 1
[7,9],    # 2
[9,10],
[6,10],
[1,2]
]
# print( "  : " ,A[0][1])
# print( "  : " ,A[1][1])
# print( "  : " ,A[2][1])
# print( "  : " ,A[3][1])
# print("length : ",len(A))
n= len(A) 
print("length -1 : ",n)
for i in range ( 0,n):
  # for j in range(0,2,1):
    j   = 1
    # print( "i : ",i  ," ","j = ",j," " ,A[i][j])
    # # print(A[i][j+1])
    # if(A[i][j])
    if( A[i][1] >= A[i+1][0]):
      print("matches at : ",A[i][1]," and ", A[i+1][0])
      A.__add


def findMatchingFriends(A):
    new2Darray = []
    for  i in range( 0,n):
      #  j = 1
       for j in range(0,1):
         if(A[i][j] >= A[i+1][j-1]):
            print("matching at :",A[i][j] , " and ", A[i+1][j-1] )

# print("hjamzaf nasser")
start = time.time()
# Result = findMatchingFriends(A)
end   = time.time()
runtime = end - start
print("The Runtime of the program is : ", runtime)   
# print("Resulting Array is : ",Result) 
