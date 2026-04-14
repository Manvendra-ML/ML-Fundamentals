import numpy as np

a= np.array([[1,2,3,4],[10,24,3,4],[25,32,41,52],[12,54,56,98]])
# a2= np.array([1,2,3,4],[1,2,3,4])

#statistical opertaions

print(a.sum())
print(a.min())
print(a.max())
print(a.max(axis=0)) # axis=0 means coloumns.
print(a.max(axis=1)) # axis=1 means rows.
print(a.sum(axis=0))
print(a.sum(axis=1))

print(a.cumsum()) # cumsum() means cumulative sum.( if you don't know cumulative sum, google it.)
print(a.cumsum(axis=0))
print(a.cumsum(axis=1))

print(np.mean(a))
print(np.median(a))

print(np.corrcoef(a)) # it does not defines for me
print(np.std(a)) # it does not defines for me