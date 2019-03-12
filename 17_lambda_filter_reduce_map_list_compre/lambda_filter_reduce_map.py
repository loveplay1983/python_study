# lambda
sum = lambda x, y: x+y
print(sum(1,1))

# map
# map(func, seq)  - Apply each of the elements of seq on func
seq = [1,2,3,4,3,3,3,3,3,3,]
f = list(map(lambda x: (float(9)/5)*x + 32, seq))  # convert celsius to fahrenheit
print(f)

# map can also be applied on more than one list object
a = [1,1,1,]
b = [2,2,2,]
c = [3,3,3,]
print(list(map(lambda a,b,c: (a+b)/c, a, b, c)))

# map will stop at the shortest list that has been consumed in which the len of lists are different

# map functions
from math import sin, cos, tan, pi

def map_func(x, funcs):
    """
    map an iterable of functions on the object x
    """

    result = []
    for each in funcs:
        result.append(each(x))
    return result

my_funcs = (sin, cos, tan)
print(map_func(pi, my_funcs))

# The above can be simplified with list comprehension
def map_func(x, funcs):
    return [ func(x) for func in funcs]

print(map_func(pi, (sin, cos, tan)))


# filtering
fibonacci = [0,1,1,2,3,5,8,13,21,34,55]
# if x % 2 == 1 then the odd number will be output
print(list(filter(lambda x: x % 2, fibonacci)))

# reduce -- reduce has been droped from the core of python3
import functools
print(functools.reduce(lambda x, y: x+y, [11,22,33,44,221,]))  # it actually has implemented a "sum"




