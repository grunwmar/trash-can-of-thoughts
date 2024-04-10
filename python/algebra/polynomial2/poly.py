
def polynomial(qlst):

    def monial(a, k):
        return lambda t: a*(t**k)

    lst = [monial(a, k) for k, a in enumerate(qlst)]
    
    def monial_sum(t):
        return sum(f(t) for f in lst)

    return monial_sum



y = poly([1,1,1])(2)

print(y)
