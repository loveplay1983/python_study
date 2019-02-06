"""
def function_name(parameter_list):
    statements - function body
    return data
"""
# ordinary form
def hello(name='xuan'):                                             # define function with optional parameter
                                                                    # docstring  - can be accessed with function_name.__doc__
    """
    hello world, this is a line of descrition for this function
    """
    print('hello {}'.format(name))                                  # print out message which means there is no returned value


# run the function
hello('world')


print('{}'.format(hello.__doc__))


# return value
def empty_rtn():
    return

print(empty_rtn())                                                  # return None

# return multiple values
def multi_rtn():
    return (1,2)

print(multi_rtn())


# local and global var
# var names are by default local to the function in which they get defined.

# global varible - we can make the variable a global version therefore anything we do to this variable inside
# the function body shall also be done to this variable outside of the function body
# example

def f():
    global g_var
    print(g_var)
    g_var = 'local_var'
    print(g_var)
g_var = 'global_var'
f()

# arbitrary number of parameters
# use *args for ordinary arguments
def get_mean(*nums):
    """
    calculates the mean of given numbers
    """
    return (sum(nums) / len(nums))

print( get_mean(1,2,2,3,3,2,2,2) )

# issue with a list of parameters
x = [1,2,2,3]
print(get_mean(*x))

x = [
     ('a', 1),
     ('b', 2),
     ('c', 3),
    ]

print(list(zip(*x)))

######################################################################
# use **kwargs if you want to use named arguments
def f(a,b):
    print(a,b)

d = {'a':1, 'b':2}
f(**d)






