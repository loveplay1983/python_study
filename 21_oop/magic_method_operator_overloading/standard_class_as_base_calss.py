"""
It is also possible to use standard classes such as 
int, float, dict or lits as base classes.
"""

class MyList(list):

    def __init__(self, l):

        list.__init__(self, l)

    def push(self, item):

        self.append(item)

if __name__ == '__main__':

    x = MyList([1, 2])
    x.push(100)
    
    print(x)
    print('\n')

