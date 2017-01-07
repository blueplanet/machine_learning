from numpy import array

mm = array((1, 1, 1))
pp = array((1, 2, 3))
print pp + mm
print pp * 2
print pp ** 2

pp = array([[1, 2, 3], [21, 22, 23]])
print pp
print pp[0, 0]

a1 = array([1, 2, 3])
a2 = array([0.3, 0.2, 0.3])
print a1 * a2
