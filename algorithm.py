from fractions import Fraction

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
    check = sum(list(map(lambda coef: coef < 0, coefficients))) == 0
    print("coefficient positiveness", check)
    return check


def extractTopZeros(coefficients):
    """
    最高時の次数の係数が0だった場合,取り除く.
    """
    if (coefficients[0] != 0):
        return coefficients

    if (len(coefficients) == 1):
        raise Error(
            "invalid coefficients Error. All of the coefficients are zeros")
    return extractTopZeros(coefficients[1:])

class BaseAlgorithm:
    def __init__(self):
        self.coefficients = []
        self.degree: int = 0
        self.equation_array=[]
        
class HurwitzStabililtyTestForRealPolymonials(BaseAlgorithm):
    """
        Algorithm 1.2

        equation_array contain coefficients
    """

    def __init__(self, coefficients=[]):
        super().__init__()
        coefficients = extractTopZeros(coefficients)
        degree = len(coefficients) - 1
        
        # check args
        if (len(coefficients) == 0):
            raise Error("No coefficients Error")
        # extract top 0s

        # 係数の政府の判定
        if not areCoefficiensPositive(coefficients):
            raise Error(
                "invalid Coefficients. given coefficients include negative values"
            )
        

        self.degree = degree
        self.coefficients = coefficients

    def makePolynomialQ(self, coefficients):
        Q_coefficients = []
        isEven = False

        # 数値的処理
        #mu = coefficients[0]/coefficients[1]
        mu = Fraction(coefficients[0],coefficients[1])
        # 高次の項から処理していく
        for i in range(1, len(coefficients) - 1):
            # 交互に処理を変える
            isEven = not isEven
            if isEven:
                Q_coefficients.append(coefficients[i])
                continue
            Q_coefficients.append(coefficients[i] - mu * coefficients[i + 1])
        # 定数項を加える.
        Q_coefficients.append(coefficients[-1])
        if len(Q_coefficients) != len(coefficients) - 1:
            raise Error("invalid degreen of Q")
        return Q_coefficients

    def firstStep(self, equation_array, coefficients):
        if len(equation_array) != 0:
            raise Error("given array is not empty")
        if not areCoefficiensPositive(coefficients):
            raise Error(
                "invalid Coefficients. given coefficinets include negative value"
            )
        equation_array.append(coefficients)
        return equation_array

    def secondStep(self, equation_array, number: int):
        """
         number(int): how many times
        """
        assert equation_array[number] == equation_array[-1], "mismatch number and array's length"
        if equation_array[number] != equation_array[-1]:
            raise Error("mismatch number and array's length")
        coefficients = equation_array[number]
        # メソッドの終了
        if not areCoefficiensPositive(coefficients):
            return False

        if number == self.degree - 2:
            return False

        return True

    def thirdStep(self, equation_array, coefficients):
        equation_array.append(self.makePolynomialQ(coefficients))
        return equation_array

    def execute(self):
        coefficients = self.coefficients
        equation_array = self.firstStep([], coefficients)
        check = True
        isHurwitz = False
        number = 0

        if (self.degree == 0):
            return True

        while (True):
            check = self.secondStep(equation_array, number)
            if not check:
                if number == self.degree - 2:
                    isHurwitz = True
                break
            equation_array = self.thirdStep(equation_array, equation_array[-1])
            number += 1
        self.equation_array = equation_array
        return isHurwitz


class HurwitzStabililtyTestForComplexPolymonials:
    """
        Algorithm 1.3
    """
    pass
