# how to ouput in python.
# output is one of the most aspect of any programming

######################################################################################
# ordinary output
out = open('out.info', 'w')
print('Printing out the message for out.info', file=out)
out.close()

# output for different targets
import sys
# output into sys.stdout  - default output which will print the message to the command line
# output into sys.steerr - output the message into error style
print('Error occured')

##############################################################################################
# formatted output
"""
Conversion Meaning
d Signed integer decimal.
i Signed integer decimal.
o Unsigned octal.
u Obsolete and equivalent to 'd',   i.e. signed integer decimal.
x Unsigned hexadecimal (lowercase).
X Unsigned hexadecimal (uppercase).
e Floating point exponential format (lowercase).
E Floating point exponential format (uppercase).
f Floating poi nt decimal format.
F Floating point decimal format.
g Same as "e" if ex ponent is greater than -4 or less than precision, "f" otherwise.
G Same as "E" if exponent is greater than -4 or less than precision, "F" otherwise.
c Single character (accepts integer or single character string).
r String (converts any python object using repr()).
s String (converts any python object using str()).
% No argument is converted, re   sults in a "%" character in the result.

Flag Meaning
# Used with o, x or X specifiers the value is p receded with 0, 0o, 0O, 0x or 0X respectively.
0 The conversion result  will be zero padded for numeric values.
- The converted value is left a  djusted
  If no sign (minus sign e.g.) is going to be written, a blank space is inserted before the value.
+ A sign character ("+" or "-") will precede  the conversion (overrides a "space" flag).
"""


print('%10.3e' % (356.44332))

print('%5X' %(47))  # 5 is flag, meaning to pad the output data at leftside for 5 blocks

print('$ %8.2f' % (3.131313131313131))

################################################################################################
########################### Pythonic Way of outputing###########################################
# using format method
"""
 |  format(...)
  |      S.format(*args, **kwargs) -> str
   |
    |      Return a formatted version of S, using substitutions from args and kwargs.
     |      The substitutions are identified by braces ('{' and '}').
      |
"""
# add position parameter and formatting parameters
# for example
print('{0} - {1}'.format(10, 20))                 # 0 and 1 are position index
print('{0:3d} - {1:.3f}'.format(132, 3.1414141))  # 3d and .3f are conversion meaning

"""
It's possible to left or right justify data with the format method. To this end, we can precede the formatting with a "<" (left justify) or ">" (right justify). We demonstrate this with the following examples:

"""

print('{0:<5s} {1:.2f}'.format('hello world', 3.243243)) # right justified

# using dictionary in "format"
#test_dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
#print('test_dict ', test_dic)
#for each in test_dic:
#    print('{a} - {b}'.format(a=each, b=test_dic[each]))  # notice that dictionary is unordered.
#
####################################################################################################
test_dic = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for each in test_dic:
    format_str = each + ':{' + each + '}'
    print(format_str.format(**test_dic))


"""
"locals" is a function, which returns a dictionary with the current scope's local variables, i.e- the local variable names are the keys of this dictionary and the corresponding values are the values of these variables:

The dictionary returned by locals() can be used as a parameter of the string format method. This way we can use all the local variable names inside of a format string.

"""
a = 10
b = 11
print('a = {a}, b = {b}'.format(**locals())) # it actually input the a=10 and b=11 as its parameters

#######################################################################################################
# other formatting method
# center, ljust, rjust and zfill
# put the str at the central position, left justify and right justify, zero padding

###############################################################################################################
# formatted string literals - prefixed with an 'f' "NEW FEATURE SINCE python3.6+" where you can just put the prefix f and
# add the "{expression}" right after, insted of using .format(**)

a = 10
print(f'this is a : {a}')
# it won't work since we have python3.5 locally in the testing env


