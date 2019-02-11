# function decorator
# class decorator

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
print(a(1),b(1))





