class Polynomial:
    def __init__(self, coeffs):
        self.coeffs = list(coeffs[:])
        while True:
            if len(self.coeffs) > 0 and self.coeffs[0] == 0:
                self.coeffs.remove(self.coeffs[0])
            else:
                break

    def __str__(self):
        return "Polynomial(coeffs={})".format(str(self.coeffs))

    def coeff(self, index):
        return self.coeffs[-index-1]

    def evalAt(self, x):
        reversed_coeffs = self.coeffs[::-1]
        result = 0
        for i in range(len(reversed_coeffs)):
            result += reversed_coeffs[i] * x ** i
        return result

    def __eq__(self,other):
        if isinstance(self, Polynomial):
            if len(self.coeffs) == 1:
                return self.coeffs[0] == other
            if len(self.coeffs) == 0:
                return other == 0
            if not isinstance(other, Polynomial):
                return False
            return self.coeffs == other.coeffs
        return False

    def scaled(self, scale):
        coeffs = []
        for i in self.coeffs:
            coeffs.append(i * scale)
        return Polynomial(coeffs)

    def derivative(self):
        reversed_coeffs = self.coeffs[::-1]
        result = []
        for i in range(1, len(reversed_coeffs)):
            result.append(reversed_coeffs[i] * i)
        return Polynomial(result[::-1])

    def addPolynomial(self, other):
        if not isinstance(other, Polynomial):
            return None
        reversed_coeffs = self.coeffs[::-1]
        reversed_other = other.coeffs[::-1]
        if len(reversed_other) > len(reversed_coeffs):
            length = len(reversed_other)
        else:
            length = len(reversed_coeffs)
        result = [0 for i in range(length)]
        for i in range(len(reversed_other)):
            result[i] += reversed_other[i]
        for i in range(len(reversed_coeffs)):
            result[i] += reversed_coeffs[i]
        return Polynomial(result[::-1])

    def multiplyPolynomial(self, other):
        reversed_coeffs = self.coeffs[::-1]
        reversed_other = other.coeffs[::-1]
        result = [0] * (len(reversed_coeffs) + len(reversed_other) - 1)
        for a, i in enumerate(reversed_coeffs):
            for b, j in enumerate(reversed_other):
                result[a + b] += i * j
        result.reverse()
        return Polynomial(result)

    def degree(self):
        return self.coeffs[0]

    def __hash__(self):
        return hash(tuple(self.coeffs))


class Quadratic(Polynomial):
    def __init__(self, coeffs):
        self.coeffs = list(coeffs[:])
        while True:
            if len(self.coeffs) > 0 and self.coeffs[0] == 0:
                self.coeffs.remove(self.coeffs[0])
            else:
                break
        if len(self.coeffs) != 3:
            return False

    def __str__(self):
        return "Quadratic(a={}, b={}, c={})".format(self.coeffs[0], self.coeffs[1], self.coeffs[2])

    def discriminant(self):
        return self.coeffs[1] ** 2 - 4 * self.coeffs[0] * self.coeffs[2]

    def numberOfRealRoots(self):
        discr = self.discriminant()
        if discr > 0:
            return 2
        if discr == 0:
            return 1
        return 0

    def getRealRoots(self):
        number = self.numberOfRealRoots()
        discr = self.discriminant()
        if number == 0:
            return []
        if number == 1:
            return [(-self.coeffs[1]) / (2 * self.coeffs[0])]
        return sorted([(-self.coeffs[1] + discr ** (1 / 2)) / (2 * self.coeffs[0]),
                (-self.coeffs[1] - discr ** (1 / 2)) / (2 * self.coeffs[0])])




