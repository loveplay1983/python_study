"""
In one perspective they are the same: You can iterate with a for loop over iterators and iterables. Every iterator is also an iterable, but not every iterable is an iterator. E.g. a list is iterable but a list is not an iterator! An iterator can be created from an iterable by using the function 'iter'. To make this possible the class of an object needs either a method '__iter__', which returns an iterator, or a '__getitem__' method with sequential indexes starting with 0.

Iterators are objects with a '__next__' method, which will be used when the function 'next' is called.

So what is going on behind the scenes, when a for loop is executed? The for statement calls iter() on the object ( which should be a so-called container object ), which it is supposed to loop over. If this call is successful, the iter call will return return an iterator object that defines the method __next__() which accesses elements of the object one at a time. The __next__() method will raise a StopIteration exception, if there are no further elements available. The for
loop whill terminate as soon as it catches a StopIteration exception. You can call the __next__() method using the next() built-in function.

"""

#x = ['a', 'b', 'c']
#iterator_obj = iter(x)
#print(type(iterator_obj))
#print(next(iterator_obj))
#print(next(iterator_obj))
#print(next(iterator_obj))
#print(next(iterator_obj)) # error raised since there is no more element within the iterator
#
#
# using iter() function to turn objects into iterator and call __next__ or loop through the data
a = {'a':1, 'b':2, 'c':3}
b = iter(a.items())
for i in b:
    print(i)


def is_iterable(obj):
    try:
        iter(obj)
        return True
    except TypeError:
        return False

test_list = [1,2,2,1,1,'a','b',[12,1,1,1,1], {'a':1, 'b':2}]
for each in test_list:
    print(each, 'iterable:', is_iterable(each))

###########################################################################################
# to make this even more clearer, check the class down below
class Reverse:
    """
    Creates iterators for looping over a sequence backwards.
    """

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

# test for Reverse class
l_test = [33,1122,-9]

l_test_backwards = Reverse(l_test)

for each in l_test_backwards:
    print(each)







