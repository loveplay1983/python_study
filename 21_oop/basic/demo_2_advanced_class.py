"""
Encapsulation
Data Abstraction
Polymorphism
Inheritance
"""

############################## Define class methods##########################
"""
Instead of defining a function outside of a class definition and binding it to a class attribute, we define a method directly inside (indented) of a class definition.
A method is "just" a function which is defined inside of a class.
The first parameter is used a reference to the calling instance.
This parameter is usually called self.
Self corresponds to the Robot object x.

"""

################### __init__ method ########################################
class RobotA:
    """
    Description of Robot
    """
    
    def __init__(self, name=None):
        self.name = name                    # Similar to this.name = name in `Java`
        
    def say_hi(self):
        if self.name:
            print('Hi, I am ' + self.name)
        else:
            print('Hi, I am a robot without name.')




x = RobotA()
x.say_hi()

y = RobotA('Jack.')
y.say_hi()



# Data abstraction, encapsulation and info hiding
# Abstraction = encapsulation + info_hiding

# Getter and Setter
class RobotB:


    def __init__(self, name=None):
        self.name = name

    def say_hi(self):
        if self.name:
            print('Hi, I am' + self.name)
        else:
            print('Hi, I am a robot without name.')

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

x = RobotB()
x.set_name('Hello')
print('Hi, my name is ' + x.get_name())


#################### __str__ and __repr__ ###################################
# __str__ and __repr__ often defined within the class definition which will be called 
# when applying str or repr method to the object and python will look for the corresponding 
# __str__ or __repr__ magic methods definition

class RobotC:
    pass

robot_c = RobotC()
print(robot_c)                             # The default output
#<__main__.RobotC object at 0x7f2ce962d0b8>

class RobotD:
    
    def __init__(self):
        pass

    def __str__(self):
        return "hi, this is " + type(self).__name__ + " with str()"

    def __repr__(self):
        return "Hi, this is " + type(self).__name__ + " with repr()"

robot_d = RobotD()
print(robot_d)                             # The modified output of class RobotD

print(str(robot_d))                        # It looks like the print() method call the str() method as its default behavior
print(repr(robot_d))                       # Print out the robot_d str info by repr() method

# __str__ vs __repr__
# __str__                                  # If the output for end useror or in other words, it should be nicely printed.
# __repr__                                 # __repr is used for internal representation of an object or in other words a string 
                                           # which can be parsed by python interpreter. The result of this parsing is in an equal object.

                                           # o == eval(repr(o)), since eval() method run the python within the program
                                           # ``` the eval() method runs the python code (which is passed as an argument) within the program.``` from 
                                           # https://www.programiz.com/python-programming/methods/built-in/eval.

l = [1, 2, 3]
s = repr(l)
print(type(s))
print(l == eval(s))

import datetime
today = datetime.datetime.now()
print(today)

str_s = str(today)
print(type(str_s))

#print(type(eval(str_s)))                   # eval can only b applied on strings created by repr

"""
Traceback (most recent call last):
  File "demo_2.py", line 119, in <module>
    print(type(eval(str_s)))
  File "<string>", line 1
    2019-03-25 13:10:34.301495
          ^
SyntaxError: invalid token

"""

repr_s = repr(today)
print(type(repr_s))

print(type(eval(repr_s)))

print(today == eval(repr_s))

########################## __str__ and __repr__ in class definition ###########
class Robot:

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year

    def __repr__(self):
        return "Robot('" + self.name + "', " + str(self.build_year) + ")" 
    
    def __str__(self):
        return "Name: " + self.name +  ", Build Year: " + str(self.build_year) + ")"

robot = Robot('John', 1975)
print(robot)

#robot_str = str(robot)
robot_repr = repr(robot)

#print(robot_str)
print(robot_repr)

#print("Type of robot_str: ", type(robot_str))
print("Type of robot_repr: ", type(robot_repr))

#new = eval(robot_str)
new = eval(robot_repr)
print(new)
print(type(new))

# It is not possible to call the eval(str(obj)), rather you have to replace str(obj) by repr(obj)
"""
Type of robot_str:  <class 'str'>
Traceback (most recent call last):
  File "demo_2.py", line 160, in <module>
    new = eval(robot_str)
  File "<string>", line 1
    Name: John, Build Year: 1975)
        ^
SyntaxError: invalid syntax

"""

####################### conclusion of __str__ and __repr__ #####################
# __str__   - For final representation, normally it is just for ordinary output
# __repr__  - For internal representation, normally it will be used to enjoy the intermediate python code


