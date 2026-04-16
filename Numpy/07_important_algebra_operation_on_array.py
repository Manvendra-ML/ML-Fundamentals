import numpy as np

a1=np.array([[1,3],[1,4]])
a2=np.array([[12,2,6,24],[1,2,9,4]])

a3=a1*a2
print(a3) # print basic multiplication on a1 and a2.

a4=a1@a2
print(a4) # print matrixs multiplication on arrays a1 and a2.

a3=np.transpose(a1)
print(a3) 

a5= np.trace(a2)
print(f"trace of matrix a2 is {a5}")

a6=np.linalg.inv(a1)
print(a6)

n=np.array([1,2])
x= np.linalg.solve(a1,n)
print (f"solution of matrixs is {x}")