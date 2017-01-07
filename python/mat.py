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

mm = mat([2, 3, 1])
mm.sort()
print mm

dd = mat([4, 5, 1])
print dd.argsort()
print dd
print 'dd.mean()', dd.mean()

jj = mat([[1, 2, 3], [8, 8, 8]])
print 'shape(jj)', shape(jj)
print 'jj[0, :]', jj[0, :]
print 'jj[1, :]', jj[1, :]
print 'jj[:, 0]', jj[:, 0]
print 'jj[:, 1]', jj[:, 1]

print 'jj[0, 0:2]', jj[0, 0:3]
