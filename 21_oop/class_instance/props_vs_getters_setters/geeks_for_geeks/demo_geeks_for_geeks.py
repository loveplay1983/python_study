"""
Syntax: property(fget, fset, fdel, doc)

Parameters:
fget() – used to get the value of attribute
fset() – used to set the value of atrribute
fdel() – used to delete the attribute value
doc() – string that contains the documentation (docstring) for the attribute

Return: Returns a property attribute from the given getter, setter and deleter.
"""
class Alphabet:
    """
    class without @property 
    """

    def __init__(self, val):

        self.__value = val

    def get_val(self):

        print('Getting value')
        return self.__value


    def set_val(self, val):

        print('Setting value to ' + val) 

    def del_val(self):

        print('Deleting the value')
        del self.__value


    value = property(get_val, set_val, del_val, )


class Alphabet2:
    """
    Class with @property
    """

    def __init__(self, val):

        self.__val = val

    @propert
    def value(self):
        print('Getting value')
        return self.__val

    @value.setter
    def value(self, val):
        print('Setting value' + val)
        self.__val = val

    @value.deleter
    def value(self):
        print('Deleting value')
        del self.__val
