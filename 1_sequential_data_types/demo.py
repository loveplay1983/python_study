# strings, byte sequences, byte arrays, lists, tuples, range objects

# unlike other programming languages, python uses the same syntax and
# function names to work on sequential data types

countries = ['China', 'USA', 'Korea', 'Japan']
nine_num = [1,2,3,4,5,6,7,8,9]

print(len(countries), len(nine_num))


# byte objects is a sequence of small integers, in the range of
# 0 through 255, corresponding to ASCII chars.

# pyton lists
# list can be minipulated by slicingo
l1 = [1,2,3,4,5,6]
print(l1[-1])  # last element
print(l1[0:2])
print(l1[::-1]) # counter-clockwise
# list allows sublist within
list_in_list = [[['a', 'b', 'c'], [1,2,3,4]]]
for i in list_in_list:
    print(i)

print(list_in_list[0][1])

# tuple is immutable list object, it cannot be changed in anyway
# benefits of tuples
# faster than list, store the data that won't have to change forever
#------------------------------------------------------------
# tuple can be used as key in dictionary while list cannot |
#------------------------------------------------------------

tuple_1 = ('1', 'b', 'III')
for i in tuple_1:
    print(i)

# check if element is contained in list
x = [1,2,3]
if 1 in x:
    print('i am in')
else:
    print('i am afk')

if 4 not in x:
    print('i am away')
else:
    print('i am in')


# pitfall of repetition of list
x = [1,2,3]
y = x * 4
z = [x] * 4
print(y)
print(z)

x[1] = 'two'
print(z)  # the * sign creates reference repetition aswell
# [[1, 'two', 3], [1, 'two', 3], [1, 'two', 3], [1, 'two', 3]]




