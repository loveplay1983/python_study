"""
The __call__ method can be used to turn the instances of the class into callables. Functions are callable objects. A callable object is an object which can be used and behaves like a function but might not be a function.

class Foo:
    def __init__(self, a, b, c):
        # ...

x = Foo(1, 2, 3) # __init__


class Foo:
    def __call__(self, a, b, c):
        # ...

x = Foo()
x(1, 2, 3) # __call__

"the __init__ method is used when the class is called to initialize the instance, while the __call__ method is called when the instance is called"


"""



class Polynomial:

    # parameters with * sign means it has arbitrary number of parameters for the current function definition
    def __init__(self, *coefficients):

        self.coefficients = coefficients[::-1]

    def __call__(self, x):
        
        res = 0
        for index, coeff in enumerate(self.coefficients):
            res += coeff * x** index
        return res

   
p1 = Polynomial(42)

p2 = Polynomial(0.4, 2)

p3 = Polynomial(1, -0.5, 0.44, 2)

for i in range(1, 3):
    print(i, p1(i), p2(i), p3(i))


# So class with __call__ is so called "callable" 
# The callable object can use class instance like function


