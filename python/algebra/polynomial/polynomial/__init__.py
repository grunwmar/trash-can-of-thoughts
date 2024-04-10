from ._methods import _poly_trim, _poly_add, _poly_neg, _poly_mul
from ._methods import _poly_poly_mul, _poly_div, _poly_poly_div
from ._repr_methods import _repr_power, _repr_operator_fmt, _repr_parentheses
from ._repr_methods import _repr_final_format, _repr_variable_fmt, _repr_prefix
from numbers import Number
from typing import Self


class Polynomial:

    def __init__(self, *coefficients: Number):
        self._coefficients = coefficients

    @property
    def list(self):
        return self._coefficients

    def __add__(self, polynomial: Self) -> Self:
        p = _poly_add(self.list, polynomial.list)
        return self.__class__(*p)

    def __sub__(self, polynomial: Self) -> Self:
        p = _poly_add(self.list, _poly_neg(polynomial))
        return self.__class__(*p)

    def __rmul__(self, m: Number) -> Self:
        if not isinstance(m, Number):
            raise ValueError(f"Argument m must be a number not a '{m.__class__.__name__}'")
        return self.__class__(*_poly_mul(self.list, m))

    def __xor__(self, polynomial: Self) -> Self:
        p = _poly_poly_mul(self.list, polynomial.list)
        return self.__class__(*p)

    def __truediv__(self, q: Number) -> Self:
        if not isinstance(q, Number):
            raise ValueError(f"Argument q must be a number not a '{q.__class__.__name__}'")
        return self.__class__(*_poly_div(self.list, q))

    def __or__(self, polynomial: Self) -> Self:
        if not isinstance(polynomial, self.__class__):
            raise ValueError(f"Argument polynomial must be a {self.__class__.__name__} instance")
        q, r = _poly_poly_div(self.list, polynomial.list)
        return self.__class__(*q), self.__class__(*r)

    def __floordiv__(self, polynomial: Self) -> Self:
        return (self | polynomial)[0]

    def __mod__(self, polynomial: Self) -> Self:
        return (self | polynomial)[1]

    def __str__(self) -> str:
        name = self.__class__.__name__
        args = ", ".join([str(i) for i in self.list])
        return f"{name}({args})"

    def __repr__(self) -> str:
        return self.__str__()

    def __call__(self, value: Number) -> Number:
        return sum(c * (value ** i) for i, c in enumerate(self._coefficients))

    def repr(self, variable: str, pretty=False, reverse=False) -> str:
        monoms = []

        def power(a): return _repr_power(a, pretty)
        def operator_fmt(a): return _repr_operator_fmt(a, pretty)
        def variable_fmt(a): return _repr_variable_fmt(a, pretty)
        def parentheses(a): return _repr_parentheses(a, pretty)
        def final_format(a): return _repr_final_format(a, pretty)
        def var_prefix(a): return _repr_prefix(a, pretty)

        if len(self._coefficients) == 1:
            if self._coefficients[0] == 0:
                return var_prefix(variable) + "0"

        for i, c in enumerate(self._coefficients):
            if c != 0:
                if i == 0:
                    monoms += [f"{c}"]
                else:
                    c = parentheses(c)
                    if i == 1:
                        monoms += [f"{c}{operator_fmt("*")}{variable_fmt(variable)}"]
                    else:
                        monoms += [f"{c}{operator_fmt("*")}{variable_fmt(variable)}{operator_fmt("**")}{power(i)}"]
        if reverse:
            return var_prefix(variable) + final_format(" + ".join(monoms[::-1]))
        else:
            return var_prefix(variable) + final_format(" + ".join(monoms))


def pretty_string(*polynomials: Polynomial, separator: str = ",  ", variable: str = "x", reverse: bool = True) -> str:
    reprs = []
    for p in polynomials:
        reprs.append(p.repr(variable, reverse=reverse, pretty=True))
    return separator.join(reprs)
