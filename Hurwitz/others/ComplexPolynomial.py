from utils import Error,HurwitzBase,extractTopZeros

class HurwitzStabililtyTestForComplexPolymonials(HurwitzBase):
    """
        Algorithm 1.3
    """

    def __init__(self, coefficients):
        self.coefficients = extractTopZeros(coefficients)
        self.degree = len(coefficients) - 1

    def firstStep(self, coefficients):
        """
        Returns
        ___
        P_array
        ____

        """
        P_array = []
        P_array.append(coefficients)
        return P_array

    def secondStep(self, P_array, number: int):
        """

        Returns
            result : boolean
        """

        assert number == len(P_array)-1, "mismatch number and array's length"
        if number != len(P_array)-1:
            raise Error("mismatch number and array's length")

        # Complex coefficients
        coefficients = P_array[number]

        # verify the coefficients
        if len(coefficients) < 2:
            return False
            #Error("invalid coefficients length")

        return (coefficients[0].real * coefficients[1].real +
                coefficients[0].imag * coefficients[1].imag > 0)

    def thirdStep(self, P_coefficients):
        # 最高次の係数が0でない
        if P_coefficients[0] == 0:
            print("todo handle in thirdStep")
            pass

        mu = (1/P_coefficients[0])
        # Todo
        T = list(map(lambda each_coefficient: each_coefficient * mu, P_coefficients))
        return T

    def fourthStep(self, old_P_array, Q_coefficients):
        P_array = old_P_array
        P_array.append(Q_coefficients)
        return P_array

    def makePolynomialQ(self, T_coefficients):
        # 定数項を忘れずに
        n = len(T_coefficients) - 1
        if n == 0:
            print("todo handle in makePolynomialQ")
            pass

        mu = 1 / T_coefficients[1]

        # 偶数回目の処理かどうか
        isEven = True
        # 諸侯だけ最初に
        Q_coefficients = []
        # 定数項の処理だけは除く
        for i in range(1, len(T_coefficients) - 1):
            coefficient = None
            if isEven:
                coefficient = complex(
                    T_coefficients[i].real,
                    T_coefficients[i].imag - mu*T_coefficients[i + 1].imag
                )
            else:
                coefficient = complex(
                    T_coefficients[i].real - mu*T_coefficients[i + 1].real,
                    T_coefficients[i].imag
                )
            Q_coefficients.append(coefficient)
            isEven = not isEven
        # 定数項の処理
        Q_coefficients.append(T_coefficients[-1])
        return Q_coefficients

    def execute(self):
        isHurwitz = False
        coefficients = self.coefficients
        P_array = self.firstStep(coefficients)
        number = 0

        while (True):
            check = self.secondStep(P_array, number)
            if not check:
                if number == self.degree - 1:
                    assert len(P_array[-1])-1 == 1 , "mismatch last array's degree"
                    isHurwitz = True
                break
            T_coefficients = self.thirdStep(P_array[-1])
            Q_coefficients = self.makePolynomialQ(T_coefficients)
            P_array = self.fourthStep(
                old_P_array=P_array, Q_coefficients=Q_coefficients)
            number += 1
        self.P_array = P_array
        return isHurwitz
