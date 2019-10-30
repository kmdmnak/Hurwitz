
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

from random import random


def makeRandomCoefficients(dim, isReal, maxRange=5, minRange=0,):
    """
    o : 0-1
    -2~2:
        (O - 0.5)*4
    -3~5:
        o*8-3
    """
    if isReal:
        return[random() * (maxRange - minRange) + minRange for w in range(dim + 1)]
    return[complex(random() * (maxRange - minRange) + minRange, random() * (maxRange - minRange) + minRange) for w in range(dim + 1)]


def randomTest(number=1000, dim=4, isReal=True):
    count = 0
    while (count < number):
        coefficients = makeRandomCoefficients(dim, isReal)
        if isReal:
            H = HurwitzStabililtyTestForRealPolymonials(coefficients)
        else:
            H = HurwitzStabililtyTestForComplexPolymonials(coefficients)
        result = H.execute()
        result_solve = solve(coefficients, ploting=False)
        if result != result_solve:
            print("Mismatch Result !!")
            print(coefficients)
            print()
        count += 1


if __name__ == "__main__":
    if sys.argv[1] == "0":
        """
        coefficients = [
            1+3j, 4+2j, 2+1j, 4+1j
        ]
        H = HurwitzStabililtyTestForComplexPolymonials(coefficients)
        """
        #coefficients = [3, 6, 4, 3, 7, 4, 5]
        coefficients = [
            1+3j, 4+2j, 2+1j, 4+1j
        ]
        #H = HurwitzStabililtyTestForRealPolymonials(coefficients)
        H = HurwitzStabililtyTestForComplexPolymonials(coefficients)
        result = H.execute()
        result_solve = solve(coefficients, True)
        print(H.P_array)
        if result:
            print("this is hurwirtz")
        print("\n")
        if result == result_solve:
            print("Same Result !!")
        else:
            print("Mismatch Result !!")
    elif sys.argv[1] == "1":
        values = [
            0.47874720357941836-0.19821029082774066j,
            1.1999999999999997-0.26666666666666655j
        ]
        print(values[0].real * values[1].real -
              values[0].imag * values[1].imag)
    elif sys.argv[1] == "2":
        randomTest(number=3000, dim=4,isReal=False)

"""
H = algorithm.HurwitzStabililtyTestForComplexPolymonials([
    1+1j, 2+3j, 4+6j,4+1j
])
print(H.execute())
print(H.P_array)
"""
