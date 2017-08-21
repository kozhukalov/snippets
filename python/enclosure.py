def fmaker(i):
    return lambda x : i * x

def multipliers():
    return [lambda x : i * x for i in range(4)]

def multipliers2():
    return [fmaker(i) for i in range(4)]

print [m(2) for m in multipliers()]
print [m(2) for m in multipliers2()]