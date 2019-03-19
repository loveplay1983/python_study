# Kinds of errors
"""
1.typos
2. semantic error
"""


# Unit test
"""
1. One can define "unit testing" as a method whereby individual units of source code are tested to determine if they meet the requirements
2. Testing one unit should be independent from the other units
"""

# Module test
"""
Every module has a name which is defined in built-in attribute __name__, when running the python script such as `python xyz.py`, the __name__ will be the string __main__
"""

""" Fibonacci Module """

def fib(n):
    """ Calculates the n-th Fibonacci number iteratively """
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def fiblist(n):
    """ creates a list of Fibonacci numbers up to the n-th generation """
    fib = [0,1]
    for i in range(1,n):
        fib += [fib[-1]+fib[-2]]
    return fib

if fib(0) == 0 and fib(10) == 55 and fib(50) == 12586269025:
    print("Test for the fib function was successful!")
else:
    print("The fib function is returning wrong values!")

# Module test by importing the fib.py script whereby to make the use of __name__ clearer

import fib
# Test for the fib function was successful! the content of the print() function was printed
# What if we don't want this message instead of just to import the functions or classes within this script file
# We can use the following line of code to avoid this kind of problem
"""
if __name__ == '__main__':
    if fib(0) == 0...
    else:....
"""

#################################################################################################################
# Unittest
"""
The Python module unittest is a unit testing framework, which is based on Erich Gamma's JUnit and Kent Beck's Smalltalk testing framework. The module contains the core framework classes that form the basis of the test cases and suites (TestCase, TestSuite and so on), and also a text-based utility class for running the tests and reporting the results (TextTestRunner).
The most obvious difference to the module "doctest" consists in the fact that the test cases of the module "unittest" are not defined inside of the module, which has to be tested. The major advantage is clear: program documentation and test descriptions are separate from each other. The price you have to pay on the other hand consists in an increase of work to create the test cases.
"""
import unittest 
from fib import fib

class FibTest(unittest.TestCase):

    def test_calculation(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10),55 )
        self.assertEqual(fib(20), 6765)

if __name__ == '__main__':
    unittest.main()





