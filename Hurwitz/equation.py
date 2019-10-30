from numpy.polynomial.polynomial import Polynomial
import matplotlib.pyplot as plt
from numpy import linspace,zeros

def solve(coefficients):
    f = Polynomial(list(reversed(coefficients)))
    
    # Solve f(x) == 0.
    X, Y = [], []
    roots = f.roots()
    print("polynomial: ", f)
    print("roots: ",roots)
    for each_root in roots:
        root = complex(each_root)
        X.append(root.real)
        Y.append(root.imag)
    plt.scatter(X, Y,s=3)
    axisLine = linspace(-10, 10)
    plt.plot(zeros(axisLine.shape),axisLine,c="red")
    plt.show()