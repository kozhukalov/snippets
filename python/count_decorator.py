#!/usr/bin/env python



COUNT = {}

def count_decorator(func, *args, **kwargs):
    print func.__name__
    def new_func(*args, **kwargs):

        if func.__name__ not in COUNT:
            COUNT[func.__name__] = 0
        COUNT[func.__name__] += 1
        return func(*args, **kwargs)

    return new_func


@count_decorator
def my_test_func(a, b, c=1):
    pass


@count_decorator
def my_test_func2(*args):
    pass

my_test_func(1, 2)
my_test_func(3, 5)
my_test_func2(1, 2, 3)


print COUNT
