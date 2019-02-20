# https://www.cnblogs.com/cicaday/p/python-decorator.html
# http://blog.51cto.com/10836356/2112490

# __call__ callable object
class Test():
    def __call__(self):
       #print('It is callable.')
        return

t = Test()
t()


# class decorator
"""
1. Define __init__() for a function
2. Overload __call__() and return a function
"""

class Logging():
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print('[DEBUG - class decorator]: enter function {func}()'.format(func=self.func.__name__))
        return self.func(*args, **kwargs)

@Logging
def say(sth):
    print('say{}!'.format(sth))



say(' Hello World!!!')


# class decorator with parameter
# To make a class decorator with parameter is slightly complicated than pure class decorator in which the constructor is no longer for receive the input function, instead it takes the input parameters for the decorator and the __call__ magic method is used to `take the input function and return the function`.

class Logging():
    def __init__(self, level='INFO'):
        self.level = level

    def __call__(self, func):                           # Accept input function
        def wrapper(*args, **kwargs):
            print('[{level}]: enter function {func}()'.format(
                level=self.level,
                func=func.__name__
                ))
            func(*args, **kwargs)
        return wrapper

@Logging(level='INFO')
def say(sth):
    print('say {}!'.format(sth))

say('class decorator with parameters')

# Built-in decorator
# Built-in decorator returns class object instead of function
"""
def getx(self):
    return self._x

def setx(self, value):
    self._x = value

def delx(self):
    del self._x

# create a property
x = property(getx, setx, delx, "I am doc for x property")

"""
# Similar to Java, we can use decoator with @ symbol and make it much easier
"""
@property
def x(self): ...

# 等同于

def x(self): ...
x = property(x)
"""
