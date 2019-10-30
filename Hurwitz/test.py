
from hurwitzTest import HurwitzStabililtyTestForComplexPolymonials, HurwitzStabililtyTestForRealPolymonials
from equation import solve

"""
5x^4 + 3x^3 +1 x^2 +0 +5
=>
[5,3,1,0,5]

coeffiecient=[5,3,1,0,5]
Q_coeffiecient=[3,1,0,5]

WRONG!!
coefficients = [
    1+3j,4+2j,2+1j,4+1j
]

"""

import sys
# coefficients=[3,6,4,3,7,4,5]
#H = HurwitzStabililtyTestForRealPolymonials(coefficients)
if __name__ == "__main__":
    if sys.argv[1] == "0":
        coefficients = [
            1+3j, 4+2j, 2+1j, 4+1j
        ]
        H = HurwitzStabililtyTestForComplexPolymonials(coefficients)
        print(H.execute())
        print(H.P_array)

        solve(coefficients)
    elif sys.argv[1] == "1":
        values = [
            0.47874720357941836-0.19821029082774066j,
            1.1999999999999997-0.26666666666666655j
        ]
        print(values[0].real*values[1].real-values[0].imag*values[1].imag)

"""
H = algorithm.HurwitzStabililtyTestForComplexPolymonials([
    1+1j, 2+3j, 4+6j,4+1j
])
print(H.execute())
print(H.P_array)
"""
