from functools import wraps

def greeting(func):
    @wraps(func)
    def function_wrapper(x):
        """ function wrapper of greeting """
        print('Hi, ' + func.__name__ + ' returns:')
        return func(x)
    return function_wrapper


