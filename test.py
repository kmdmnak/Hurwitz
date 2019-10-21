import algorithm

"""
5x^4 + 3x^3 +1 x^2 +0 +5
=>
[5,3,1,0,5]

coeffiecient=[5,3,1,0,5]
Q_coeffiecient=[3,1,0,5]
"""
#H = algorithm.HurwitzStabililtyTestForRealPolymonials([5,3,1,0,5])
H = algorithm.HurwitzStabililtyTestForRealPolymonials([-1,0,1])
print(H.execute())
print(H.equation_array)