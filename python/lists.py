def extend_list(val, list=[]):
    list.append(val)
    return list



print extend_list(10)
print extend_list(100, [])
print extend_list('a')