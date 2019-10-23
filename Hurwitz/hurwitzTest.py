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
    """
        入力された係数が全て正か調べる.
    """
    check = sum(list(map(lambda coef: coef < 0, coefficients))) == 0
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
        self.coefficients = None
        self.degree: int = None
        self.P_array = None


class HurwitzStabililtyTestForRealPolymonials(HurwitzBase):
    """
        Algorithm 1.2
    """

    def __init__(self, coefficients):
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
        if coefficients[1] == 0:
            print("あとでやる")
            raise Error("zero divide")
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
        if number != len(P_array)-1:
            raise Error("mismatch number and array's length")

        coefficients = P_array[number]
        # メソッドの終了
        if not areCoefficiensPositive(coefficients):
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

            print("coefficient positiveness", check)
            if not check:
                break

            if number == self.degree - 2:
                isHurwitz=True
                break

            P_array = self.thirdStep(
                old_P_array=P_array, Q_coefficients=P_array[-1])
            number += 1
        self.P_array = P_array
        return isHurwitz


class Coefficients:
    def __init__(self, array_like):
        self.coefficients = array_like


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
        if P_coefficients[0] == 0:
            # TODO
            print("あとでやる")
            raise Error("zero division")

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

        if T_coefficients[1] == 0:
            raise Error("zero divition")

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
        """
        isHurwitz (boolean) : whether this polynomial is stable

        Return
        ____
        isHurwitz(boolean)
        ____
        """
        isHurwitz = False
        coefficients = self.coefficients
        P_array = self.firstStep(coefficients)
        number = 0

        while (True):
            check = self.secondStep(P_array, number)
            if not check:
                if number == self.degree - 1:
                    assert len(P_array[-1]) - \
                        1 == 1, "mismatch last array's degree"
                    isHurwitz = True
                break
            T_coefficients = self.thirdStep(P_array[-1])
            Q_coefficients = self.makePolynomialQ(T_coefficients)
            P_array = self.fourthStep(
                old_P_array=P_array, Q_coefficients=Q_coefficients)
            number += 1
        self.P_array = P_array
        return isHurwitz
