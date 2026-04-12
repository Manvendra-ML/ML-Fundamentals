import numpy as np

a1=np.array([1,2,3])
a2=np.array([1.3,2,.13,4.4,5,6.5])

print(a1.dtype) # print data type of array a1
print(a2.dtype) # print data type of array a2

print(a1.itemsize) # print size of single element of arrray a1
print(a2.itemsize) # print size of single element of arrray a2

print(a1.nbytes) # print size of total element of arrray a1
print(a2.nbytes) # print size of total element of arrray a2

print(a1.data) # abhi pata nhi kis kaam ka h
print(a2.data) # abhi pata nhi kis kaam ka h

print(a1.strides) # abhi pata nhi kis kaam ka h
print(a2.strides) # abhi pata nhi kis kaam ka h