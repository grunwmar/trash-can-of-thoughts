from numbers import Number


def _repr_power(n: int, pretty: bool) -> str:
    if pretty:
        nums = {
            0: "⁰",
            1: "¹",
            2: "²",
            3: "³",
            4: "⁴",
            5: "⁵",
            6: "⁶",
            7: "⁷",
            8: "⁸",
            9: "⁹",
        }
        return nums[n]
    return str(n)


def _repr_operator_fmt(o: str, pretty: bool) -> str:
    if pretty:
        ops = {
            "*": "",
            "**": "",
        }
        return ops[o]
    return o


def _repr_parentheses(c: Number, pretty: bool) -> str:
    if not pretty:
        return f"{c}" if c > 0 else f"({c})"
    if c == 1:
        return ""
    elif c == -1:
        return "-"
    return f"{c}"


def _repr_variable_fmt(var: str | Number, pretty: bool) -> str:
    if isinstance(var, str):
        if len(var) == 1:
            return var
    return f"({var})"


def _repr_final_format(string: str, pretty: bool) -> str:
    if pretty:
        return string.replace(" + -", " - ")
    return string


def _repr_prefix(var: str, pretty: bool) -> str:
    if pretty:
        return f"{var} → "
    return f"{var} -> "
