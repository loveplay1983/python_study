"""
A callable object is an object which canbe used and behaves like a function
but might not be a function, hence, it is possible to define classes in a way
that the instances will be callable object
"""


# __call__
class A:

    def __init__(self):                                        # Constructor
        print('An instance of A was initialized')


    def __call__(self, *args, **kwargs):                       # __call__ built-in function, hence, a callable object
        print('Arguments are: ', args, kwargs)


