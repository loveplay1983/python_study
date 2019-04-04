"""
The attributes of objects are stored in a dictionary "__dict__". Like any other dictionary, a dictionary used for attribute storage doesn't have a fixed number of elements. In other words, you can add elements to dictionaries after they have been defined, as we have seen in our chapter on dictionaries. This is the reason, why you can dynamically add attributes to objects of classes that we have created so far
"""
class A:

    pass


a = A()
a.x = 100
a.name = 'hello world'



"""
You might have wondered that you can dynamically add attributes to the classes, we have defined so far, but that you can't do this with built-in classes like 'int', or 'list'
"""

"""
Using a dictionary for attribute storage is very convenient, but it can mean a waste of space for objects, which have only a small amount of instance variables. The space consumption can become critical when creating large numbers of instances.

Slots are a nice way to work around this space consumption problem. Instead of having a dynamic dict that allows adding attributes to objects dynamically, slots provide a static structure which prohibits additions after the creation of an instance.
"""


class S:

    __slots__ = ['val']                                         # __slots__ defines all the attributes that are available
                                                                # Attributes are all unavailable other than ones defined within __slots__

    def __init__(self, v):

        self.val = v

if __name__ == '__main__':
    x = S(10)
    print(x.val)

    x.new = 'hello world'


