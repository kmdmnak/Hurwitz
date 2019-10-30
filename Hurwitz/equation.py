from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt
from numpy import linspace, zeros


def solve(coefficients, ploting=True):
    f = Polynomial(list(reversed(coefficients)))

    # Solve f(x) == 0.
    X, Y = [], []
    roots = f.roots()
    print("polynomial: ", f)
    print("roots: ", roots)
    result = areRootsRealPositive(roots)
    
    if ploting:
        for each_root in roots:
            root = complex(each_root)
            X.append(root.real)
            Y.append(root.imag)
        plt.scatter(X, Y, s=3)
        axisLine = linspace(-10, 10)
        plt.plot(zeros(axisLine.shape), axisLine, c="red")
        plt.show()
    return result


def areRootsRealPositive(roots):
    return sum(list(map(lambda x: x.real > 0, roots))) == 0
