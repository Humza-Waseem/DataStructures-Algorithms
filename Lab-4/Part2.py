#############################    PRINTING THE 2D-ARRAY / MATRIX   ##############################
# def printMatrix(A, starting_index, rows, columns):
#     row_start, col_start = starting_index
#     for i in range(rows):
#         for j in range(columns):
#             print(A[row_start + i][col_start + j], end=" ")
#         print()

# # Example usage
# A = [[ 3, 4, 5], [2,5,7]]
# starting_index = (0, 2)
# rows = 1
# columns = 2

# printMatrix(A, starting_index, rows, columns)



#############################    Adding 2 Matrices   ##############################

# def MatAdd(A, B):
#     rows = len(A)
#     columns = len(A[0])
#     C = [[0 for _ in range(columns)] for _ in range(rows)]
#     # C = [[0,0],[0,0]]
#     for i in range(rows):
#         for j in range(columns):
#             C[i][j] = A[i][j] + B[i][j]

#     return C
# A = [[1,3,5],
#              [7,9,11]]
# B = [[2,4,6],
#              [8,10,12]]
# C = MatAdd(A, B)
# n = len(A)
# print("Length : ",n)
# print(C)

# #############################    MatAddPartial 2 Matrices   ##############################
# def MatAddPartial(A,B,start,size):
#     first,second  =  start
#     for i in range(size):
#         for j in range(size):
#             C =  A[first + i],[second + j] + B[first + i],[second + j]
#     print(C)


# A = [[1, 2, 3, 4], [5, 12, 7, 8], [9, 10, 11, 12]]
# B = [[13, 14, 15, 16], [17, 18, 19, 20], [29, 22, 23, 24]]
# start = (1, 2)
# size = 2

# MatAddPartial(A, B, start, size)