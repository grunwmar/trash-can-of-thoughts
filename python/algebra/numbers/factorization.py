# factorization
import itertools

def fcrgen(n: int):
    f = 2
    increments = itertools.chain([1,2,2], itertools.cycle([4,2,4,2,4,6,2,6]))
    for incr in increments:
        if f*f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n


def factors(n):
    dct = dict()

    for i in fcrgen(n):
        try:
            dct[i] += 1
        except KeyError as e:
            dct[i] = 0
        else:
            dct[i] += 1

    return dct

factors(100)
