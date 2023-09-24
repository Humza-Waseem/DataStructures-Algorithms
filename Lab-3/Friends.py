import time

#funtion to find matching time for friends
def findMatchingFriends(A,n):
  num = []
  for i in range ( 0,n):
  
    if( A[i][1] >= A[i+1][0]):
      print("matches at : ",A[i][1]," and ", A[i+1][0])
      num = num + [A[i][1], A[i+1][0]] 
      # print(num)
  return num

    
###############################    Taking the Input    #############################

A= [[1,4],    [2,5],  [7,9],    [9,10],[6,10],[1,2]]
n= len(A) -1
start = time.time()
result = findMatchingFriends(A,n)
end   = time.time()
runtime = end - start
print("The Runtime of the program is : ", runtime)   
print("Matching Times for the friends : ",result)
