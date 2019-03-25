"""
Encapsulation
Data Abstraction
Polymorphism
Inheritance
"""


# Basice class form
class Robot():
    """
    A basic class consists of keyword `class` and class-name `Robot`, 
    use `pass` at the time being since we are not going to implement 
    any methods or return anything.
    """
    
    pass


def f(x):
    
    return 42



if __name__ == '__main__':
    x = Robot()
    y = Robot()

    y2 = y
    print(y == y2)
    print(y == x)
    print(y2 == x)


# Attributes - Properties
# Attribute and property are used interchargeably

# Attribute can be add by the class instance
    x.name = 'Marvin'
    x.build_year = '2019'

    y.name = 'Caliban'
    y.build_year = '2018'

    print(x.name, x.build_year)
    print(y.name, y.build_year)


# Use __dict__ to show all the attributes and their corresponding values of a class
# Notice __dict__ is just a dictionary which stores the attribute bundles
    print(x.__dict__)
    print(y.__dict__)


# Attributes can be bound to the class name too
    z = Robot()
    Robot.brand = 'Kuka'

    print(z.brand)
    print(Robot.brand)
    
# Check __dict__ with class name directly
    print(Robot.__dict__)

# Exception raises if one calls the non-existing attribute 
    #print(z.hello)
# One can prevent such exception by getattr() method
    print(getattr(z, 'hello', 'world'))      # 'hello'   - attribute var name
                                             # 'world'   - attribute var value
                                             

# Function can also add arbitrary name and value
    f.x = 100                                # def f(x): return 42
    print(f.x)

############################## Define class methods##########################
"""
Instead of defining a function outside of a class definition and binding it to a class attribute, we define a method directly inside (indented) of a class definition.
A method is "just" a function which is defined inside of a class.
The first parameter is used a reference to the calling instance.
This parameter is usually called self.
Self corresponds to the Robot object x.

"""

################### __init__ method ########################################




