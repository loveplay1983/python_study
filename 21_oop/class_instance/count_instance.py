"""
to create a class attribute, which we call "counter" in our example
to increment this attribute by 1 every time a new instance will be create
to decrement the attribute by 1 every time an instance will be destroyed

"""

class Count:

    """
    Create a class in which it will be used to count the number of instance it would be initialized.
    """

    # The class attribute is the key too make this counter to count the num of instance successfully
    # It is of course will count the repetition of initialization since class attribute lives in a global scope 
    # in which it is shared by all the instances.
    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1


if __name__ == '__main__':

    x = Count()
    print('Number of instances - ' + str(Count.counter))

    y = Count()
    print('Number of instances - ' + str(Count.counter))
