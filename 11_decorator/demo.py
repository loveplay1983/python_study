# function decorator
# class decorator
# General purpose function
def nl():
    print('\n')

"""
A decorator in Python is any callable Python object that is used to modify a function or a class. A reference to a function "func" or a class "C" is passed to a decorator and the decorator returns a modified function or class. The modified functions or classes usually contain calls to the original function "func" or class "C".
"""

# 1. It is possible to assign multiple names to the same function
def  f1(x):
    return (x+1)
f2 = f1
print(f1(1))
print(f2(1))
# 2. One can delete one of the names which points to the same function without
# taking effect to the original function itself.

del f1
print(f2(1))

print('\n' * 2)
# function inside of function
# this concpet is new to c/c++ programmer
def f():

    def g():
        print('it is g()')
        print('g() is done')

    print('this is the f()')
    print('f() is done')
    g()

f()

# return statements in functions
def f():

    def g():
        return ('g()')
    result = 'it is ' + g() + ' and f() returned'
    return result

print(f())

print('\n' * 2)
#### Now function as parameter
"""
 Due to the fact that every parameter of a function is a reference to an object and //functions are objects as well//, we can pass functions - or better "references to functions" - as parameters to a function.
"""

def g():
    print('it is g()')
    print('g() is done')

def f(func):
    print('it is f(func)')
    print('f(func) about to call g()')
    func()
    print('real name of func ->' + func.__name__)
f(g)

print('\n' * 2)
### function returning function
def f(x):
    def g(y):
        return (y+x+3)
    return g

a = f(1)
b = f(2)
print (a, '\n', b)
print('\n'*3)
#print(a(1),b(1))


# define a function for polynomial function
def gen_poly(*coefs):
    """
    coefficients are in the form of a_0, a_1, ...a_n
    """

    def poly(x):
        res = 0
        for index, coef in enumerate(coefs):
            res += coef * x** index
        return res
    return poly

p1 = gen_poly(4)
p2 = gen_poly(2, 4)
p3 = gen_poly(2, 3, -1, 8, 1)
p4 = gen_poly(-1, 2, 1)

for x in range(-2, 2, 1):
    # print(x)
    print(x, '  ', p1(x), p2(x), p3(x), p4(x))
print('\n'*3)

# Simple decorator
def simple_decorator(func):
    def func_wrapper(x):
        print('Before calling -> ' + func.__name__)
        func(x)
        print('After calling -> ' + func.__name__)
    return func_wrapper

def foo(x):
    print('foo has been called with ' + str(x) + '\n')

print('call foo before decoration')
foo('hey foo\n')

print('call foo with decoration')
foo = simple_decorator(foo)

print('call foo after decoration')
foo(1)

print('\n'*3)

############################################################################
# Usual syntax for decorator
"""
foo existed in the same program in two versions, before decoration and after decoration which is causing a lot of confusion and hard to read about.
we can use "@" symbol to indicate that out implementation is about decoration
"""

# Rewrite the above code as it is a more proper form as how the decoration should work

def my_decorator(func):
    def func_wrapper(x):
        print('before dec')
        func(x + ' world')
        print('after dec')
    return func_wrapper

@my_decorator
def foo(x):
    print(x, 'foo is about to be decorated.')

foo('hello')

nl()

# It is possible to decorate 3rd party functions. e.g. functions that we import form a module, but we cannot use "@" symbol in this case
from math import sin, cos

def my_decorator(func):
    """
    Decoration with 3rd party functions
    """

    def function_wrapper(x):
        print('Before calling ' + func.__name__)
        result = func(x)
        print(result)
        print('After calling ' + func.__name__)

    return function_wrapper

sin = my_decorator(sin)
cos = my_decorator(cos)

for each in [sin, cos]:
    nl()
    each(3.1415)

nl()

# Makeing decorator to accept arbitrary parameters
from random import random, randint, choice

def my_decorator(func):
    """
    Making the decorator function can accept arbitaray parameters
    in order to modify the function more vesatilely
    """
    def wrapper(*args, **kwargs):
        print(func.__name__, 'before decoration')
        result = func(*args, **kwargs)
        print(result)
        print(func.__name__, 'after decoration')
    return wrapper

random = my_decorator(random)
randint = my_decorator(randint)
choice = my_decorator(choice)

random()
nl()
randint(3, 8)
nl()
choice([4,3,3313,1])
nl()



