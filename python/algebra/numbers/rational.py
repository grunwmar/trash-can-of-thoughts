from math import gcd

RATIONAL_STR = "{dividend}/{divisor}"
class Rational(object):


    def __init__(self, a:int, b:int):
        self._val = (int(a), int(b))
        self.normalize()

    def normalize(self):
        a, b = self._val
        c = gcd(a, b)
        q1 = a // c
        q2 = b // c

        self._val = (q1, q2)

    def __str__(self):
        a, b = self._val
        q, r = a // b, a % b
        return RATIONAL_STR.format(dividend=a, divisor=b, quotient=q, remainder=r)

    def __repr__(self):
        return self.__str__()


    def remainder(self, rational=True):
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

    #TODO: Arithmetic operations!!