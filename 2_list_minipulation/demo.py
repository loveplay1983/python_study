# push - append method
# pop - return the most upper element of the stack
# peek - return the last element of the stack without removing it, [-1]


a = [1,2,3,4,5]
a.append('one')
a.pop(2) # remove the element of the corresponding indices
last = a[-1]
print(a, last)


# extend - adding more than one element (append for single element)
x = [1,2]
y = ['3', '4']
#x.append(y)
#print(x)
x.extend(y)
print(x)

# + and += for append extend
x = [1,1,1,1]
y = [2,2,2,2]
print(x + [y])

# don't do L = [1,2] L = L + [22]
# instead, the appropriate alternative is L += [22]
# compare the above code by time.time()
import time
n = 100000

#start = time.time()
#l = []
#for i in range(n):
#    l = l + [i * 2] # NOT PRACTICAL IN REALITY
#print(time.time() - start)

start = time.time()
l = []
for i in range(n):
    l += [i * 2]
print(time.time() - start)

start = time.time()
l = []
for i in range(n):
    l.append(i * 2)
print(time.time() - start)

# conclusion
"""
code like a = a + 2 tend to call a 2 times
where a += 2 will call a only once
it is the reason why a += 2 has better performance
"""

# remove an element
# remove the element without knowning the position
a = [1,2,3,4]
print('a was', a)
a.remove(2)
print(a)

# find pos of element
#s.index('data', start, stop)
a = [1,2,3,4]
print(a.index(1))

# append only add the element right after the most recent or the last element you already have,
# to make it even more efficiently, we use "insert" which will help to add the element to arbitrary position

#s.insert(pos, 'data')

#a = [1,2,3,4]
#a.insert(1, 'two')
#print(a)
#
# simulate append by insert
a = [1,2,3,4]
a.insert(len(a), 'ttwo')
print(a)



