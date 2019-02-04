# shallow copy referes to the sitution when coping or assigning simple data types
# like integers or strings where deep copy is only relevant for compound objects,
# i.e. objects contaning other objects like lists or class instances

################################################################################

# shallow copy example
l1 = [1,2,3]
l2 = l1
print('before cp', l1, l2)

l2[0] = 11
print('after cp', l1, l2, '\n')

# both l1, l2 share the memory location, once you change l2, l1 changes too

l1 = [1,2,3,[11,22,33]]
l2 = l1[:]
print('before cp', l1, l2)

l2[0] = 0
print('after cp', l1, l2, '\n')

# after copying l1 to l2 by "colon - : sign", both l1, l2 become
# independently, but sub list remain the same, they share the memory location as before

# test for sub list
print('before changing sub list for l2', l1, l2)
l2[3][0] = 111
print('after changing sub list for l2', l1, l2, '\n')

# use deep copy strategy to overcome the problem of deeper structural data

from copy import deepcopy

l1 = [1,2,[11,22]]
l2 = deepcopy(l1)

print(l1, l2, '\n')

# id both l1 and l2
print(id(l1), id(l2))






