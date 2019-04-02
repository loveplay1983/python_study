class A:
    def m(self):
        print("m of A called")

class B(A):
    def m(self):
        print("m of B called")
    
class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    pass


"""
If you call the method m on an instance x of D, i.e. x.m(), we will get the output "m of B called". If we transpose the order of the classes in the class header of D in "class D(C,B):", we will get the output "m of C called". 
"""


class A:
    def m(self):
        print("m of A called")

class B(A):
    pass

class C(A):
    def m(self):
        print("m of C called")

class D(B,C):
    pass

x = D()
x.m()

# Different results from calling python2 or python3
#$ python diamond1.py
#m of A called                 # Old-style class, depth-first then left to right
                               # Python2.7 with new-style class must explicitly inherited from `object`
#$ python3 diamond1.py
#m of C called                 # New-style class, breadth-first 
                               # Python3.x with new-style class is okay without explicit inheritance from `object`
                               # The interpreter is set to use new-style class by default.
#

"""
Only for those who are interested in Python version2:
To have the same inheritance behaviour in Python2 as in Python3, every class has to inherit from the class "object". Our class A doesn't inherit from object, so we get a so-called old-style class, if we call the script with python2. Multiple inheritance with old-style classes is governed by two rules: depth-first and then left-to-right. If you change the header line of A into "class A(object):", we will have the same behaviour in both Python versions.
"""





