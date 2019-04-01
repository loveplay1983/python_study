class P:

    """
    Class P defines __init__ by passing input to another set_x directly
    which means it initialize the input value accordingly.

    The private __x is bound to the class instance instead of class itself.

    """
    def __init__(self,x):
        
        self.set_x = x
                                            # This breaking the interface in which the attribute x is not available anymore

    def get_x(self):
  
        return self.__x

    def set_x(self, x):

        if x < 0:
            self.__x = 0

        elif x > 1000:
            self.__x = 1000

        else:
            self.__x = x


# Proper way to define class for encapsulation
class P1:
    
    def __init__(self, x):
      
        self.x = x                          #############################################################################################################
                                            # Now the definition is more flexible which you can input your data and the class P1 has hidden the interface
                                            #############################################################################################################                                           

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x



# Redefine the class without decorator @property
class P2:

    def __init__(self,x):
        self.__set_x(x)

    def __get_x(self):
        return self.__x

    def __set_x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

    # property is defined withint builtin.py
    x = property(__get_x, __set_x)

###############################################################################
### The version with the decorator "@property" is the Pythonic way to do it!  # 
###############################################################################



# Many attributes are only internally needed and creating interfaces for the user of the class increases unnecessarily the usability of the class. The possible user of a class shouldn't be "drowned" with umpteen - of mainly unnecessary - methods or properties! 
class Robot:

    def __init__(self, name, build_year, lk=0.5, lp=0.5):
        
        self.name = name
        self.build_year = build_year
        self.__potential_physical = lk
        self.__potential_psychic = lp

    @property
    def condition(self):

        s = self.__potential_physical + self.__potential_psychic

        if s <= -1:
            return 'I feel miserable!'
        elif s <= 0:
            return 'I feel bad!'
        elif s <= 1:
            return 'Seems to be okay!'
        else:
            return 'Great!'



