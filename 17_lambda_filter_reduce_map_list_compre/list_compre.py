# The author of python language Guido van Rossum adovcates "list comprehension" over lambda, filter, reduce...

# convert fahrenheit to celsius
celsius = [1,1,1,1,1,1,11,]
fahrenheit = [((float(9)/5)*x + 32) for x in celsius]
for each in fahrenheit:
    print(each)


# pythagorean triple
pythagorean = [(x, y, z) for x in range(1, 30) for y in range(x, 30) for z in range(y, 30) if x**2 + y**2 == z**2]
for each in pythagorean:
    print(each)

# another example of picking things from different source and ouput together
a = [1,2,3]
b = ['a', 'b', 'c']
a_b = [(x, y) for x in a for y in b]
print(a_b)

# generator comprehension
a = ( x**2 for x in range(20) )
print(a)
a = list(a)
print(a)


# recursive fuinction to calculate primes
from math import sqrt
def primes(n):
    if n == 0:
        return []
    elif n == 1:
        return []
    else:
        p = primes(int(sqrt(n)))
        no_p = {j for i in p for j in range(i*2, n+1, i)}
        p = {x for x in range(2, n+1) if x not in no_p}
    return p

for i in range(1, 50):
    print(i, primes(i))
