from polynomial import Polynomial, pretty_string


if __name__ == "__main__":

    p = Polynomial(-3, 1)
    q = Polynomial(2, 1)
    r = Polynomial(1, 1)

    s = p ^ q ^ r

    print(p, q, r)
    print(s)

    print(pretty_string(p,q,r, separator=",   "))
    print(pretty_string(s, separator=""))