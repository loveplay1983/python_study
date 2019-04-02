"""
The order is defined by the so-called "Method Resolution Order" or in short `MRO`.

"""


class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
    
#class C(A):
#    def m(self):
#        print("m of C called")
#
#class D(B,C):
#    def m(self):
#        print("m of D called")
#
#x = D()
#B.m(x)
#
#
#B.m(A())
#B.m()


b = B()
b.m()

B.m()                           # m() is not a class method but an instance method instead 
                                # which means it must be called with `self`, i.e. it is an instance method

"""
TypeError: m() missing 1 required positional argument: 'self'

"""


###############################  super() ###################################################################

class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
        super().m()

class C(A):
    def m(self):
        print("m of C called")
        super().m()

class D(B,C):
    def m(self):
        print("m of D called")
        super().m()


#>>> from super5 import D
#>>> x = D()
#>>> x.m()
#m of D called
#m of B called
#m of C called
#m of A called
#

# The above code represents the mechanism of Python3 class in which it frist search on the horizontal direction,
# then search for the vertical direction.


###########  The super function is often used when instances are initialized with the __init__ method  #############

class A:
    def __init__(self):
        print("A.__init__")

class B(A):
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A):
    def __init__(self):
        print("C.__init__")
        super().__init__()


class D(B,C):
    def __init__(self):
        print("D.__init__")
        super().__init__()
