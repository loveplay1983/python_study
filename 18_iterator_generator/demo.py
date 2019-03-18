# https://nvie.com/posts/iterators-vs-generators/

"""
Containers are data structures holding elements, and that support membership tests. They are data structures that live in memory, and typically hold all their values in memory, too. In Python, some well known examples are:

    list, deque, …
    set, frozensets, …
    dict, defaultdict, OrderedDict, Counter, …
    tuple, namedtuple, …
    str

"""

# An object is a container when it can be possibly asked whether it contains a certain element within
print(1 in [1, 2,])

# Dict object will check the keys
d1 = {1:'hello world', 2:'python'}
print(1 in d1.keys())
print(1 in d1)

# It is also feasible to ask a string
s1 = 'hello world'
print('h' in s1)

"""
Not all containers are necessarily iterable. An example of this is a Bloom filter. Probabilistic data structures like this can be asked whether they contain a certain element, but they are unable to return their individual elements.
"""

x = [1, 2, 3]
y = iter(x)
print(next(y))
print(next(y))
print(next(y))
#print(next(y))     # An StopIteration will occur

# Here x is an iterable and y, z are iterator

"""
Often, for pragmatic reasons, iterable classes will implement both __iter__() and __next__() in the same class, and have __iter__() return self, which makes the class both an iterable and its own iterator. It is perfectly fine to return a different object as the iterator, though.
"""

# Using dis.dis to disassemble the python code for better understanding of what is iteralbe and iterator
import dis
x = [1,2,3]
dis.dis('for i in x: pass')
"""
 1           0 SETUP_LOOP              12 (to 14)
              2 LOAD_NAME                0 (x)
              4 GET_ITER
        >>    6 FOR_ITER                 4 (to 12)
              8 STORE_NAME               1 (i)
             10 JUMP_ABSOLUTE            6
        >>   12 POP_BLOCK
        >>   14 LOAD_CONST               0 (None)
             16 RETURN_VALUE

"""
# So an iterator is any object that has a __next__() method which is can be treated as a value factory, each time you ask it for the "next" value, it knows how to compute it return it since it holds the interval state.
# Examples of iterator
from itertools import count
counter = count(start=1)
for i in range(20):
    print(next(counter))

# Infinite sequences from finite sequences
from itertools import cycle
colors = cycle(['red', 'green', 'blue'])

# Produce finite sequences from infinite sequences
from itertools import islice
colors = cycle(['red', 'green', 'blue'])
limited = islice(colors, 0, 4)
for each in limited:
    print(each)
 
# To sum up, iterator is like a lazy factory which is idle until you ask it for a certain value

# Generator
# Key facts to remember - Any iterator is a iterable not vice versa
#                       - Any iterator is therefore lazily produce value which is a "lazy factory"

def fib():
    prev, curr = 0, 1
    while True:
        yield curr
        prev, curr = curr, prev+curr

f = fib()
print(list(islice(f, 0, 10)))


# There are 2 types of generator
num = [1,2,3,4,]
# Generator expression
# List comprehension
print([x * x for x in num])

# Set comprehension
print({x *x for x in num})

# Dict comprehension
print({x: x * x for x in num})

# Generator expression
gen_exp = (x * x for x in num)
print(gen_exp)

print(next(gen_exp))
print(next(gen_exp))
print(list(gen_exp))

# Generator function
# Any function that contain "yield" within its body




