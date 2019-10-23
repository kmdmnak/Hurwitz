from fractions import Fraction
from utils import Error,HurwitzBase,extractTopZeros,areCoefficiensPositive

class HurwitzStabililtyTestForRealPolymonials(HurwitzBase):
    """
        Algorithm 1.2
    """

    def __init__(self, coefficients=[]):
        super().__init__()
        self.coefficients = extractTopZeros(coefficients)
        self.degree = len(coefficients) - 1

        # check args
        if (len(self.coefficients) == 0):
            raise Error("No coefficients Error")
        # extract top 0s

        # 係数の政府の判定
        if not areCoefficiensPositive(self.coefficients):
            raise Error(
                "invalid Coefficients. given coefficients include negative values"
            )

    def makePolynomialQ(self, coefficients):
        Q_coefficients = []
        isEven = True

        # 数値的処理
        #mu = coefficients[0]/coefficients[1]
        mu = Fraction(coefficients[0], coefficients[1])
        # 高次の項から処理していく
        for i in range(1, len(coefficients) - 1):
            if isEven:
                Q_coefficients.append(coefficients[i])
            else:
                Q_coefficients.append(
                    coefficients[i] - mu * coefficients[i + 1])
            # 交互に処理を変える
            isEven = not isEven
        # 定数項を加える.
        Q_coefficients.append(coefficients[-1])
        if len(Q_coefficients) != len(coefficients) - 1:
            raise Error("invalid degreen of Q")
        return Q_coefficients

    def firstStep(self, coefficients):
        P_array = []

        if not areCoefficiensPositive(coefficients):
            raise Error(
                "invalid Coefficients. given coefficinets include negative value"
            )
        P_array.append(coefficients)
        return P_array

    def secondStep(self, P_array, number: int):
        """
         number(int): how many times
        """
        assert number == len(P_array)-1, "mismatch number and array's length"
        if number == len(P_array)-1:
            raise Error("mismatch number and array's length")

        coefficients = P_array[number]
        # メソッドの終了
        if not areCoefficiensPositive(coefficients):
            return False

        if number == self.degree - 2:
            return False

        return True

    def thirdStep(self, old_P_array, Q_coefficients):
        P_array = old_P_array.copy()
        P_array.append(self.makePolynomialQ(Q_coefficients))
        return P_array

    def execute(self):
        coefficients = self.coefficients

        # contain coeffients of each step.
        P_array = self.firstStep(coefficients)
        check = True
        isHurwitz = False
        number = 0

        if (self.degree == 0):
            return True

        while (True):
            check = self.secondStep(P_array, number)
            if not check:
                if number == self.degree - 2:
                    isHurwitz = True
                break
            P_array = self.thirdStep(
                old_P_array=P_array, Q_coefficients=P_array[-1])
            number += 1
        self.P_array = P_array
        return isHurwitz