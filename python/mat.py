from numpy import mat, matrix
from numpy import shape
from numpy import multiply

ss = mat([1, 2, 3])
print ss

mm = matrix([1, 2, 3])
print mm

print mm[0, 0]

array = [5, 11, 13]
print mat(array)

print ss * mm.T

print shape(ss)
print shape(mm.T)
print shape(ss * mm.T)

print multiply(mm, ss)
