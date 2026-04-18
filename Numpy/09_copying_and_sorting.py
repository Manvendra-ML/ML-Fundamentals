import numpy as np 

a1=np.array([[1,2,4,3],[12,4,23,15]])

print(a1.sort())

b1=a1 
print(b1) 

print( b1 is a1)
b1[1][0] =100
print(b1)
print(a1) # by this methode we just give a second name to the array.

c =a1.view()
print ( c is a1)
c[0][2]=200 # changing in c.
print(f"c is {c}") # changing in c, this also effect a1.

d=np.copy(a1)
print(d is a1)
d[0][3] # changing in d.
print(a1) # changing in d, there is no change in a1



