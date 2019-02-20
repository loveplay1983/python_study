"""
Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behaviour of function or class. Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it.

"""
class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self):
        # some code can be added before the function call

        self.function()

        # some code can be added again after the function call

# adding decorator to the class
@MyDecorator
def function():
    print('GeeksforGeeks.')

function()                                               # Same as function = MyDecorator()


# Class decorator with *args **kwargs
class MyDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):                 # Arbitrary args
        self.function(*args, **kwargs)

@MyDecorator
def function(name, msg='hello world'):
    print('{} - {}.'.format(name, msg))

function('xuan')

# Class decorator with return statement
class SquareDecorator:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        result = self.function(*args, **kwargs)
        return result

@SquareDecorator
def get_square(n):
    print('Given number is: ', n)
    return n*n

print('Square of this number is: ', get_square(10))

# Using class Decorators to print Time required to execute a program
from time import time
class Timer:
    def __init__(self, func):
        self.function = func

    def __call__(self, *args, **kwargs):
        start = time()
        result = self.function(*args, **kwargs)
        end = time()
        print('Execution took {} seconds'.format(end-start))
        return result

@Timer
def execution_test(delay):
    from time import sleep
    sleep(delay)

#execution_test(5)


# Checking error parameter using class decorator
"""
This type of class decorators is the most frequently used, the decorator checks parameters before executing the function
preventing the function to become overloaded and enables it to store only logical and necessary statements.
"""

class NumOnly:
    def __init__(self, function):
        self.function = function

    def __call__(self, *params):
        if any([isinstance(i, str) for i in params]):
            raise TypeError('parameter cannot be a string')
        else:
            return self.function(*params)

@NumOnly
def add_nums(*nums):
    return sum(nums)

print(add_nums(1,2,3))
print(add_nums('1',2,3))









