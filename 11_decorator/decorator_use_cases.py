# Checking args with decorator
def arg_check(f):
    def test(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception('Input is not Integer.')
    return test


@arg_check
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1, 10):
    print(i, '- ', factorial(i))


print(factorial(-1))

