import numpy as some

# creation empty array
n1=some.empty((2,2),int)
print(n1)

# creation 0s array
n2=some.zeros((2,2),int)
print(n2)

# creation 1s array
n3=some.ones((2,2),int)
print(n3)

# creation full array
n4=some.full((2,2),10)
print(n4)

# creating array with random values
n5=some.random.random((4,2))
print(n5)

# using arange function in array
n6=some.arange(10)
print(n6)
n7=some.arange(0,100,5)
print(n7)

# using linespace function
n8=some.linspace(0,5,5)
print(n8)