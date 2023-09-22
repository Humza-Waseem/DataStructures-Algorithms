# import math
# import os
# import random
# import re
# import sys

# def compareTriplets(a, b):
#     # Write your code here
#     arr = []
#     sumAlice = 0
#     sumBob = 0
#     for i in range (0,len(a) -1 ):
#         if(a[i] > b[i]):
#             sumAlice = sumAlice + 1
            
#         elif(a[i] == b[i]):
#             continue
#         elif(a[i]<b[i]):
#             sumBob = sumBob + 1
#     return arr[(sumAlice)+(sumBob)]



# a = [5,6,7]
# b = [3,6,10]
# result = compareTriplets(a,b)
# print("result is = ",result)




#################################################################


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    print(arr)

arr = [11,2,4,
       4,5,6,
      10,8,-12]