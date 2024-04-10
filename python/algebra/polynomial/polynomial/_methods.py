from itertools import zip_longest
from numbers import Number


def _poly_trim(p: list) -> list:
    while p and p[-1] == 0:
        p.pop()
    if not p:
        p.append(0)
    return p


def _poly_add(p1: list, p2: list) -> list:
    p = [x + y for x, y in zip_longest(p1, p2, fillvalue=0)]
    return p


def _poly_neg(p: list) -> list:
    p = [-x for x in p]
    return p


def _poly_mul(p: list, m: Number) -> list:
    p = [x * m for x in p]
    return p


def _poly_div(p: list, q: Number) -> list:
    p = [x/q for x in p]
    return p


def _poly_poly_mul(p1: list, p2: list) -> list:
    p1 = _poly_trim(p1)
    p2 = _poly_trim(p2)

    n1 = len(p1)
    n2 = len(p2)
    n3 = n1 * n2

    p3 = [0 for _ in range(n3)]

    for i1, a1 in enumerate(p1):
        for i2, a2 in enumerate(p2):
            p3[i1 + i2] += a1 * a2

    return _poly_trim(p3)


def _poly_poly_div(p1: list, p2: list) -> tuple[list]:
    """ src: https://stackoverflow.com/questions/26173058/division-of-polynomials-in-python """

    # Create normalized copies of the args
    num = list(_poly_trim(p1))
    den = list(_poly_trim(p2))

    if len(num) >= len(den):

        # Shift den towards right, so it's the same degree as num
        shift_length = len(num) - len(den)
        den = [0] * shift_length + den
    else:
        return [0], num

    quot = []
    divisor = float(den[-1])
    for i in range(shift_length + 1):

        # Get the next coefficient of the quotient.
        mult = num[-1] / divisor
        quot = [mult] + quot

        # Subtract mult * den from num, but don't bother if mult == 0
        # Note that when i==0, mult!=0; so quot is automatically normalized.
        if mult != 0:
            d = [mult * u for u in den]
            num = [u - v for u, v in zip(num, d)]

        num.pop()
        den.pop(0)

    num = _poly_trim(num)
    return quot, num





