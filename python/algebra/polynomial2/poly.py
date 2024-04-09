
def poly(qlst):

    def m(a, k):
        return lambda t: a*(t**k)

    lst = [m(b, k) for k, b in enumerate(qlst)]
    
    def r(t):
        return sum(f(t) for f in lst)

    return r

y = poly([1,1,1])(2)

print(y)
