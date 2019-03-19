# Example of exception in python 
# In short, the exception block in python is consist of a try except pair corresponding to language like Java in which it uses try catch block
while True:
    try:
        n = input("Please enter an integer\n")
        n = int(n)
        break
    except ValueError:
        print("No valid integer!")
print("Great, you have just entered an integer")


# Multiple exception clauses
# A try statement may have more than one except clause for different exceptions. But at most one except clause will be executed.

import sys
try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())

except IOError as e:
    errno, strerror = e.args
    print('I/O error({0}): {1}'.format(errno, strerror))
    print(e)


except ValueError:
    print('No valid integer in line')

except:
    print('Unexpected error', sys.exc_info()[0])
    raise                                               # Raise is called and all the rest of code will stop execution right off the bat 


# An except clause may name more than one exception in a tuple of error names, as we see in the following example
try:
    f = open('integers.txt')
    s = f.readline()
    i = int(s.strip())

except (IOError, ValueError):
    print('IO error has occured')
except:
    print('An unexpected error has occured.')
    raise                                               # Trigger the exception explicitly

# Exception occurs inside of a function call
def f():
    x = int('two')

try:
    f()
except ValueError as e:
    print('Exception inside of a function is catched', e)


# Now define exception within the function body and use "raise" key word to propagate the exception to the caller which in this case the try except block outside of 
# the function body, see the example below
def f():
    try:
        x = int('four')
    except ValueError as e:
        print('Exceptin catched before the try except block outside of the function body')
        raise                                           # Propagate the exception to the outside caller 
try:
    f()
except ValueError as e:
    print('Exception outside of the function body')


# Custom-made exception
#raise SyntaxError('Oh it was my fault!')                # Use of built in exception name
#
## Inherited from Exception class
#class MyExcept(Exception):                              # Use of custom exception name definition
#    pass
#
#raise MyExcept('An exception has occured and the message is shown in the way of customized.')
#
#
# Clean up actions
# try... except and finally
# Finally block will be trigger if neither try nor except was catched
try:
    x = float(input('Your num: '))
    inverse = 1.0/x
except ValueError:
    print('You should have given either int or float')
except ZeroDivisionError:
    print('Infinity')
finally:
    print('There may or may not have been an exception')

"""
The try ... except statement has an optional else clause. An else block has to be positioned after all the except clauses. An else clause will be executed if the try clause doesn't raise an exception.
"""

import sys
fn = sys.argv[1]
text = []
try:
    fh = open(fn, 'r')
    text = fh.readlines()
    fh.close()
except IOError:
    print('File cannot be opened.')

if text:
    print(text[100])

# You need to run the above script as following
# python *.py *.txt

# There is another way to achieve the same result
import sys
fn = sys.argv[1]
text = []
try:
    fh = open(fn, 'r')
except IOError:
    print('File cannot be opened.')
else:
    text = fh.readlines()
    fh.close()

if text:
    print(text[100])








