import numbers
from math import gcd, log10
from numbers import Number


RATIONAL_STR = "{numerator}/{divisor}"

class Rational(Number):

    @staticmethod
    def from_float(x, r=6):
        x = round(x, r)
        s = int(log10(abs(x))+1) + r
        exponent = 10**s

        numerator = int(x*exponent)
        divisor = exponent

        return Rational(numerator, divisor)



    def __init__(self, a:int, b:int):
        self._val = (int(a), int(b))
        self.normalize()

    def normalize(self):
        a, b = self._val
        c = gcd(a, b)
        q1 = a // c
        q2 = b // c

        self._val = (q1, q2)
        return  self

    def __str__(self):
        a, b = self._val
        q, r = a // b, a % b
        return RATIONAL_STR.format(numerator=a, divisor=b, quotient=q, remainder=r)

    def __repr__(self):
        return self.__str__()


    def strf(self, formatstr):
        a, b = self._val
        q, r = a // b, a % b
        return formatstr.format(numerator=a, divisor=b, quotient=q, remainder=r,
                                num=a, div=b, quot=q, rem=r)

    def split(self, rational=True):
        a, b = self._val
        q = a // b
        r = a % b

        if rational:
            return q, self.__class__(r, b)
        else:
            return q, r

    def __invert__(self):
        a, b = self._val
        return self.__class__(b, a)

    @property
    def divisor(self):
        return self._val[1]

    @property
    def numerator(self):
        return self._val[0]

    @property
    def tuple(self):
        return tuple(self._val)


    #TODO: Arithmetic operations!!

    def __add__(self, other):
        n1, d = self.numerator * other.divisor, self.divisor * other.divisor
        n2 = other.numerator * self.divisor
        return Rational(n1 + n2, d)

    def __sub__(self, other):
        n1, d = self.numerator * other.divisor, self.divisor * other.divisor
        n2 = other.numerator * self.divisor
        return Rational(n1 - n2, d)

    def __mul__(self, other):
        n = self.numerator * other.numerator
        d = self.divisor * other.divisor
        return Rational(n, d)

    def __truediv__(self, other):
        n = self.numerator * other.divisor
        d = self.divisor *other.numerator
        return Rational(n, d)

    def __pow__(self, other):
        if isinstance(other, numbers.Number) and not isinstance(other, self.__class__):
            n = self.numerator ** other
            d = self.divisor ** other
            return Rational(n, d)