# Checking args with decorator
def arg_check(f):
    def test(x):
        if type(x) == int and x > 0:
            return f(x)
