
class Error(Exception):
    def __init__(self, message):
        print(message)


class Equation:
    """
    an xn + a_n-1 x_n-1 + a_n-2 x_n-2 + ... + a0
    =>
    coefficients=[an,a_n-1,a_n-2,...,a_0]
    """

    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.degree = len(coefficients)-1


def areCoefficiensPositive(coefficients):
    """
        入力された係数が全て正か調べる.
    """
    check = sum(list(map(lambda coef: coef < 0, coefficients))) == 0
    print("coefficient positiveness", check)
    return check


def extractTopZeros(coefficients):
    """
    最高次の係数が0だった場合,取り除く.
    """
    if (coefficients[0] != 0):
        return coefficients

    if (len(coefficients) == 1):
        raise Error(
            "invalid coefficients Error. All of the coefficients are zeros")
    return extractTopZeros(coefficients[1:])


class HurwitzBase:
    def __init__(self):
        self.coefficients = []
        self.degree: int = 0
        self.P_array = []
        