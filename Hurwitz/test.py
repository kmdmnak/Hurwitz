
from hurwitzTest import HurwitzStabililtyTestForComplexPolymonials,HurwitzStabililtyTestForRealPolymonials

"""
5x^4 + 3x^3 +1 x^2 +0 +5
=>
[5,3,1,0,5]

coeffiecient=[5,3,1,0,5]
Q_coeffiecient=[3,1,0,5]
"""


#H = algorithm.HurwitzStabililtyTestForRealPolymonials([5,3,1,0,5])
H = HurwitzStabililtyTestForRealPolymonials([1,1,4,30])
print(H.execute())
print(H.P_array)

"""
H = algorithm.HurwitzStabililtyTestForComplexPolymonials([
    1+1j, 2+3j, 4+6j,4+1j
])
print(H.execute())
print(H.P_array)
"""