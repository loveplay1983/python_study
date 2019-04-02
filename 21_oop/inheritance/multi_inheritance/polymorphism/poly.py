"""
Python is implicitly polymorphic.
We can implement the function without writing the code for each of the different condition explicitly.
"""


def my_func(x, y):

    print('value - {0} / data type - {1}'.format(x, type(x)))
    print('value - {0} / data type - {1}'.format(y, type(y)))


my_func(1, 0.22121)
my_func(21231, 'hello world')
