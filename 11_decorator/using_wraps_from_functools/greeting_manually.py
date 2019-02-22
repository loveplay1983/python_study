def greeting(func):
    def function_wrapper(x):
        """ function wrapper of greeting """
        print('Hi, ' + func.__name__ + ' returns:')
        return func(x)
    function_wrapper.__name__ = func.__name__
    function_wrapper.__doc__ = func.__doc__
    function_wrapper.__module__ = func.__module__

    return function_wrapper


