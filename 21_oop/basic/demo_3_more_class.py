# public, protected and private attributes
"""

* Private attributes: 
  should only be used by the owner, i.e. inside of the class definition itself.
* Protected (restricted) Attributes: 
  may be used, but at your own risk. Essentially, this means that they should only be used under certain conditions.
* Public Attributes:
  can and should be freely used.
------------------------------------------------------------------------------------

* First, we can prefix an attribute name with a leading underscore "_". This marks the attribute as protected. It tells users of the class not to use this attribute unless, somebody writes a subclass. We will learn about inheritance and subclassing in the next chapter of our tutorial.

* Second, we can prefix an attribute name with two leading underscores "__". The attribute is now inaccessible and invisible from outside. It's neither possible to read nor write to those attributes except inside of the class definition itself.

"""


class A:

    def __init__(self):
        self.__priv = 'Hi there, my name is mr. private'         # Inaccessible from outside of the current class
        self._prot = 'Hey there, this is mr. protected'          # Should notbe accessed from outside, unless internal or subclass use
        self.pub = 'Hello world, this is mr. public'             # Can be accessed publicly

# Robot example 
class Robot:
    """
    A Robot class for public, protected and private attributes demo
    """

    def __init__(self, name=None, build_year=2019):
        self.__name = name
        self.__build_year = build_year

    def say_hi(self):
        if self.__name:
            print('Hi there, I am ' + self.__name)
        else:
            print('HI there, I am a Robot without name.')

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_build_year(self, by):
        self.__build_year = by 

    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return "Robot('" + self.__name + "' " + str(self.__build_year) + ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " + str(self.__build_year) 

    # The class instance can be destroied once there is no longer any reference to this instance, 
    # in that way we often take on "__del__" method
    def __del__(self):
        print('Goodbye, ' + type(self).__name__ + ' is leaving, see you next time')

# Setter and getter 
"""
class A():

    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def GetX(self):
        return self.__x

    def GetY(self):
        return self.__y

    def SetX(self, x):
        self.__x = x

    def SetY(self, y):
        self.__y = y

"""

if __name__ == "__main__":
    
    # Initialize x, y 
    x = Robot('John', 2019)
    y = Robot('Marvin', 1998)

    for each in [x, y]:
        each.say_hi()
        if each.get_name() == 'Marvin':
            each.set_build_year(1993)
        print('I was built in the year ' + str(each.get_build_year()) + '!')


    del x
    del y



