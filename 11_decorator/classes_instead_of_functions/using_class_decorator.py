def dec1(f):
    def wrapper():
        print('Decorating', f.__name__)
        f()

    return wrapper

@dec1
def foo():
    print('Inside of foo()')

foo()


# using class to implement the same effect

class dec2:

    def __init__(self, f):
        self.f = f

    def __call__(self):
        print('Decorating', self.f.__name__)

        self.f()

@dec2
def foo2():
    print('Inside of foo2')

foo2()




