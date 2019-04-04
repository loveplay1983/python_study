x = [4, 5, 9]
y = "Hello"
print(type(x), type(y))
print(type(type(x)), type(type(y)))
"""
type(classname, superclasses, attributes_dict)
"""

class A:

    pass

x = A()
print(type(x))


"""
When we call "type", the call method of type is called. The call method runs two other methods: new and init


type.__new__(typeclass, classname, superclasses, attributedict)
type.__init__(cls, classname, superclasses, attributedict)

The new method creates and returns the new class object, and after this the init method initializes the newly created object.
"""

class Robot:

    counter = 0

    def __init__(self, name):

        self.name = name

    def say_hello(self):

        return 'Hi, this is ' + self.name



# Define new robot class with type class.
# It is same to "class Robot2: pass"
def rob_init(self, name):

    self.name = name

Robot2 = type('Robot2',                   # class name
             (),                         # superclass
             { 'counter': 0,             # attributes
               '__init__': rob_init,
               'say_hello': lambda self: "Hi, this is " + self.name})

# x = Robot2('Robot2')
x = Robot2('Robot2')
print('class defined with type manually - ', x.name)
print(x.say_hello())
print('----------------------------------------')
y = Robot('Marvin')
print('class defined with class directly - ', y.name)
print(y.say_hello())


print(x.__dict__, '\n', y.__dict__)







