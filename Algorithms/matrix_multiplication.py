# Author : foxfromworld
# Date   : 24/11/2020
# O(n3)

def matrix_multiplication_original(A,B):
  # A: x*y
  # B: y*z
  # result: x*z
  result = [[0]*len(B[0]) for _ in range(len(A))] 
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        result[i][j] += A[i][k] * B[k][j]        
  return result

# https://www.programiz.com/python-programming/examples/multiply-matrix
def matrix_multiplication(A,B):
  result = [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*B)] for X_row in A]  
  return result
  
A = [[1,2,3],[4,5,6]]
B = [[10,11],[20,21],[30,31]]
#[[140, 146],
#[320 335]]       
A = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]
B = [[5,8,1,2],
    [6,7,3,0],
    [4,5,9,1]]
#[[114, 160, 60, 27]
#[74, 97, 73, 14]
#[119, 157, 112, 23]]

print(matrix_multiplication(A,B))
