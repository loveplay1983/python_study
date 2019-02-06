# parameters and arguments are often used interchangeblely by many people
# there is very import difference where args are the actual data of input and params are the defintion parts

# call by value call by reference in c or c++
# what about python???

# Correctly speaking, Python uses a mechanism, which is known as "Call-by-Object", sometimes also called "Call
# by Object Reference" or "Call by Sharing".

def ref_demo(x):
    print('x = ', x, 'id = ', id(x))
    x = 42
    print('x = ', x, 'id = ', id(x))

x = 9
print(id(x))
ref_demo(x)
print(id(x))

# x initially behaves like call-by-reference, as soon as we change
# the value of such a variable, aka as soon as we assign a new
# object to it, python "switch" to call-by-value

# side effect
# simply put, when we use a global list as argument of a function
# and if we change the data of the list within the function body
# the outside global varible is also changed

def side_effect(x):
    x += ['a', 'b']

y = [1,2]
print('without side_effect = ', y)
#side_effect(y)
#print('with side_effect = ', y)  #the list was change within function
#
# to prevent such side effect, we can pass a copy of the original input
side_effect(y[:])
print('with side_effect by passing a copy of the original input = ', y)

# sys.argv
import sys
for each in sys.argv:
    print(each)


# variable length of parameters
def test(arg1, *args):
    print(arg1, args)

test('a')
test('arg1','args')
# the positional parameter always have to be given
