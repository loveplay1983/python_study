# A set contains an unordered collection of unique and immutable objects.


# string set, output sigularized chars
x = set('hello world')
print(x)

# list set, output each element
x = set([1,2,2,3,5])  # the redundant elements are ignored
print(x)

# tuple set, output simiar to list set
x = set((1,2,2,3,5))
print(x)


# sets cannot contain mutable objects but it is mutable itself
x = set([1,2,3,3,5]) # original set
print(x)
x.add('a')  #  add new element
print(x)

############################################################
# frozensets is similar to oridinary sets but they cannot be changed

x = frozenset([1,2,3,3,5])
print('frozenset - original ', x)
#x.add('a')
#print('frozenset - add new element, you may find error gets raised', x)
#

##################################################################
# create sets without set() method, we add curly braces
x = {1,2,3,3,2,2,2,2,2,2,2} # a set with curly braces
print('set with curly braces', x)


# set operations

# add
x = {'1', 'b', 'two'}
x.add(100)
print(x)

# clear elements
x.clear()
print(x)  # set x gets cleared out.

# copy
x = {'a','b','c'}
# b = x # only creat a pointer to set "x"
b = x.copy()
x.clear()
print(x,b)

# difference of 2 sets
x = {1,2,2,3,4}
y = {1,1,1,1,1,1}
# z = x.difference(y)
# print(z)  # return the intersection of 2 sets
##################################################################
# fix it up , this isn't proper to call it is inersection here!!!
##################################################################
#
# use "-" minus sign can also do the same thing
#z = x - y
# z = y - x  # ends up with empty set, since set y has no intersection with set x from the perspective view of y
# print(z)

x = {"a","b","c","d","e"}
y = {"b","c"}
x.difference_update(y)  # generate the resulting set in-place
print(x)

a = {'a', 'b', 'c'}
b = {'a'}
a.difference_update(y)
print(a)

# discard(el)  discard an element
x = {1,2,2,3,4}
x.discard(2)
print(x)

# remove(el) works like discard(), error raised when element doesn't exist
#x ={1,2,3,43,3,2}
#x.remove('a')
#print(x)

# union
a = {1,2,3}
b = {'a', 'b', 'c'}
c = a.union(b)
print(c)

# intersection
a = {1,2,2,2,2,2}
b = {1,}
c = a.intersection(b)
print(c)

# use ampersand operator "&" for same functionality
print(a & b)

# return False if null intersection - isdisjoint()
a = {1,2,3,}
b = {'a', 'b', 'c'}
print(a.isdisjoint(b))

# issubset() issuperset()
a = {1,2,}
b = {1,2,3,}
print('is a subset of b,', a.issubset(b))
c = {1}
print('is a superset of c,', a.issuperset(c))


#### pop method
a = {1,2,2,2,2,2}
a.pop()
print(a)







