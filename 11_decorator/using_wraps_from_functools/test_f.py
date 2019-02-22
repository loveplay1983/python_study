from greeting import greeting
#from greeting_manually import greeting

@greeting
def f(x):
    """ just some silly function """
    return x + 4

f(10)
print('function name: ', f.__name__)
print('function doc: ', f.__doc__)
print('function belongs to module: ', f.__module__)



