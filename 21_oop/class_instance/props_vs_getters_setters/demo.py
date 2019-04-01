from prop_setter_getter import *
from note import *

# prop_setter_getter.py
p = P(1)
p.x = 1001                     # Our new class means breaking the interface. The attribute x is not available anymore.
                               # That's why in Java e.g. people are recommended to use only private attributes with getters and setters, 
                               # So that they can change the implementation without having to change the interface. 



print(p.x)

p1 = P1(100)

print(p1.x)                    # Since the x is a defined method followed by a decorator @property, we can call it directly just like 
                               # Calling a property and it returns the private property __x which consists of the encapsulation.
p1.x = 0
print(p1.x)                    # Because x here is followed by decorator @x.setter, we can call it directly just like calling a normal
                               # Setter function without considering much of the underlying structure.


# note.py
c = C()

c.x = 10
x = c.x
print(x)


# prop_setter_getter.py
x = Robot('Marvin', 1979, 0.2, 0.4)
print(x.condition)
