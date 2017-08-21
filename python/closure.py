
a = []

def fun_maker(i):
    def fun(x):
        return x + i
    return fun

for i in xrange(10):
    a.append(fun_maker(i))

for f in a:
    print f(10)
