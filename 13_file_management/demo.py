# To open file in python we can use "open" function with optinal flag parameters

if False:
    f = open('test.file')
    for line in f:
        print(line, end='')
    f.close()

if False:
    f = open('test.file')
    for line in f:
        print(line.rstrip())
    f.close()

# Write into file, it is as easy as open the file
if False:
    f = open('test.file', 'w')
    f.write('3.Third line of testing text...\n')
    f.close()

# Using context manager to handle read and write in a more convenient manner
if False:
    with open('test.file', 'w') as file_op:
        file_op.write('4. Fourth line of text\n')

# Open file with context manager
if False:
    with open('test.file') as file_op:
        for line in file_op:
            print(line.rstrip())

# Reading and writing simultaneously
if False:
    f_in = open('test.file')
    f_out = open('test2.file', 'w')

    i = 1
    for line in f_in:
        print(line.rstrip())
        f_out.write(line)       # copy test.file data to test2.file
        i += 1
    f_in.close()
    f_out.close()


# If you want to append something to an existing file, you have to use "a" instead of "w".
if False:
    read_f = open('test2.file').readlines()
    for line in read_f:
        print(line, type(line))


# Read the complete content of the file which includes the carriage returns and line feeds
if False:
    read_f = open('test2.file').read()
    print(type(read_f))
    for c in read_f:
        print(c)

"""
It's possible to set - or reset - a file's position to a certain position, also called the offset. To do this, we use the method seek. It has only one parameter in Python3 (no "whence" is available as in Python2). The parameter of seek determines the offset which we want to set the current position to. To work with seek, we will often need the method tell, which "tells" us the current position. When we have just opened a file, it will be zero. We will demonstrate the way of working with
both seek and tell in the following example.
"""

if False:
    f = open('test.file')
    #print(f.tell())
    #print(f.read(7))                          # index of the current reading position (excluding the index argument)
    #print(f.read(50))

    # it is also possible to set the file position
    f = open('test.file')
    print(f.read(7))
    #print(f.seek(f.tell() - 6))
    print(f.read(f.seek(f.tell() - 6)))

# w+ - create a new file if the file doesn't exist or write the data into the file
# r+ - read the file or append data to the file

########################################
# How to reread the data with "pickle"##
#######################################
"""
Python offers for this purpose a module, which is called "pickle". With the algorithms of the pickle module we can serialize and de-serialize Python object structures. "Pickling" denotes the process which converts a Python object hierarchy into a byte stream, and "unpickling" on the other hand is the inverse operation, i.e. the byte stream is converted back into an object hierarchy. What we call pickling (and unpickling) is also known as "serialization" or "flattening" a data structure.
"""

import pickle

cities = ['BeiJing', 'ShangHai', 'NewYork', 'Tokyo']

f = open('cities.pkl', 'bw')                  # bw for binary data storage
pickle.dump(cities, f)
f.close()

# read the data content back from pkl file
f = open('cities.pkl', 'rb')
cities = pickle.load(f)
print(cities)

##############################################################################################
# we can also pickel multiple objects by put the multiple python objects into another object#
############################################################################################


# shelve module vs pickle module
"""
One drawback of the pickle module is that it is only capable of pickling one object at the time, which has to be unpickled in one go. Let's imagine this data object is a dictionary. It may be desirable that we don't have to save and load every time the whole dictionary, but save and load just a single value corresponding to just one key. The shelve module is the solution to this request. A "shelf" - as used in the shelve module - is a persistent, dictionary-like object. The
difference with dbm databases is that the values (not the keys!) in a shelf can be essentially arbitrary Python objects -- anything that the "pickle" module can handle. This includes most class instances, recursive data types, and objects containing lots of shared sub-objects. The keys have to be strings.
"""

import shelve

s = shelve.open('shelve_module_test')
s['a'] = 1
s['b'] = 2
for key in s:
    print(key)

for i in s.items():
    print(i)


print(s['a'], s['b'])






