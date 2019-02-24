# How to import modules
import math, random
from math import sin, pi, cos
from math import *
from numpy import *
import numpy as np
print(np.e)
print(np.diag([3, 11, 4, 42]))


# A module is just a file containing Python definitions and statements
import fib as fi
#for i in range(10):
#    print(fi.fib(i))
#
#for i in range(10):
#    print(fi.ifib(i))
#
# To save some type we can assign the module and method to a variable, e.g.
myfib = fi.fib
for each in range(5):
    print(myfib(each))

# How to reload your moudle
import fib
from imp import reload
reload(fib)

"""
 There are different kind of modules:

 Those written in Python
 They have the suffix: .py
 Dynamically linked C modules
 Suffixes are: .dll, .pyd, .so, .sl, ...
 C-Modules linked with the Interpreter:
 It's possible to get a complete list of these modules:
 ```
 import sys
 print(sys.builtin_module_names)
 ```
An error message is returned for Built-in-Modules.
"""

# module search path
import numpy as np
print(np.__file__)
import random as rand
print(rand.__file__)


# Content of module
import math
# print(dir(math))
# Calling dir() without an argument, a list with the names in the current local scope is returned
# print(dir())

# It's possible to get a list of the Built-in functions, exceptions, and other objects by importing the builtins moduleo
import builtins
print(dir(builtins))













