# object references
x = 42
print(x)

x = 'now x references a string'
print(x)

# id
x = 42
print('id of x', id(x))

y = x
print('now x and y are the same')
print(id(x), id(y))

y = 11
print('now y is different from x')
print(id(x), id(y))

# keywords
'''
and, as, assert, break, class, continue, def, del, elif, else,
except, False, finally, for, from, global, if, import, in, is,
lambda, None, nonlocal, not, or, pass, raise, return, True, try,
while, with, yield
'''
# using underscore over camelcase

# change data types and storage locations
# number
a = 0o10  # octal
hex_num = 0xA0F # hex
bin_num = 0b101010 # bin

x = hex(19)
print(type(x))

