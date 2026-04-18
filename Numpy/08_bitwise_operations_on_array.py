import numpy as np

a1=np.array([[1,2,3,4],[5,6,7,8]])
a2=np.array([[1,1,1,1],[2,2,2,2]])

a3=np.bitwise_and(a1,a2)
print(a3)
a4=np.bitwise_or(a1,a2)
print(a4)
a5=np.bitwise_xor(a1,a2)
print(a5)

a6=np.invert(a1)
print(a6)