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
# naming convertions
# using underscore over camelcase

# change data types and storage locations
# number
a = 0o10  # octal
hex_num = 0xA0F # hex
bin_num = 0b101010 # bin

x = hex(19)
print(type(x))

x = bin(65)
print(x, chr(65))

# python can be unlimited size for data calculation
x = 787366098712738903245678234782358292837498729182728
print(x*x*x)

# division
print(1/6) # true division
print(1//6)  # floor division
# floor division is to get the most possible largest integer that is
# smaller than the result of true division

# string
# what is bigendian and littleendian
"""
Big Endian Byte Order: The most significant byte (the "big end") of the data is placed at the byte with the lowest address. The rest of the data is placed in order in the next three bytes in memory.

Little Endian Byte Order: The least significant byte (the "little end") of the data is placed at the byte with the lowest address. The rest of the data is placed in order in the next three bytes in memory.

For example, say that the 32-bit pattern 0x12345678 is stored at address 0x00400000. The most significant byte is 0x12; the least significant is 0x78.

Within a byte the order of the bits is the same for all computers (no matter how the bytes themselves are arranged).
"""

# utf-32, one to one encoding, 4 bytes num to 4 bytes memory storeage
# utf-16, 2 bytes to 2 bytes memory storage, hard to get access outside
# of 2^16
# utf-8,  variable-length encoding system for unicode, the 0-128 is
# identical to ASCII, and the later data encoding come up with so
# so called "Extended Latin" for like Chinese, Jpanese and any other
# symbols, it is much complex to find the Nth character which causes more longer time for searching.

# how to define strings in different ways
str1 = "Hello world"
str2 = 'Hi there this is python'
str3 = "Hello world python with double quotes"
str4 = """Hello world pthon with triple quotes"""

print(str1, '\n', str2, '\n', str3, '\n', str4)

# how to access string data - indexing it
print(str1[0])
print(str1[len(str1) - 1]) # last char of the string

# indexing through the whole string forwardly and backwardly
# 0,1,2... -1,-2,-3...

# slicing, concatenation, repetition, size
print(str1[1:3])
print(str1+str2)
print(str1*2)
print(len(str1))

# it is like string in "Java" but unlike "C, C++" , python strings
# cannot be changed, trying to change it will throw an error
# it is called "immutable"

# python peculiarity
# "==" and "is", "is" checks if the 2 objects have same identity
a = 'Linux'
b = 'Linux'
print(a == b)
print(a is b)

a = "Baden-Württemberg"
b = "Baden-Württemberg"
print(id(a), id(b))
print(a == b)
print(a is b)

# python3. uses the concepts of text and (binary data) of unicode
# instead of strings and 8-bits strings
# it is not possible to mix up text and ata in python3.

x = b'hello'
print(type(x))
t = str(x)
print(type(t))
u = t.encode('utf-8')
print(type(u))


"""
unicode is meant to handle text. Text is a sequence of code points which may be bigger than a single byte. Text can be encoded in a specific encoding to represent the text as raw bytes(e.g. utf-8, latin-1...).

Note that unicode is not encoded! The internal representation used by python is an implementation detail, and you shouldn't care about it as long as it is able to represent the code points you want.

On the contrary str in Python 2 is a plain sequence of bytes. It does not represent text!

You can think of unicode as a general representation of some text, which can be encoded in many different ways into a sequence of binary data represented via str.
----------------------------------------------------------------------
Note: In Python 3, unicode was renamed to str and there is a new bytes type for a plain sequence of bytes.
---------------------------------------------------------------------

DIFFERENCE BETWEEN BYTE OBJECT AND STRING OBJECT
Byte objects are sequence of Bytes, whereas Strings are sequence of characters.
Byte objects are in machine readable form internally, Strings are only in human readable form.
Since Byte objects are machine readable, they can be directly stored on the disk. Whereas, Strings need encoding before which they can be stored on disk.


"""

# encoding example

a = 'hello world'
b = b'hello world'
print(a == b)

# encode a so it turns to byte object that machine can read
c = a.encode('ASCII')
if (c == b):
    print('a is now encoded to "ASCII"')
else:
    print('failed')

# decoding
a = 'hello world'
b = b'hello world'

c = b.decode('ASCII')
if (c == a):
    print('c is decoded and it is same to a now')
else:
    print('c is diff from a')



