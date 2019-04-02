from clock import *


x = Clock(23, 59, 59)
print(x)
x.tick()
x.tick()
x.tick()
x.tick()
print(x)

y = str(x)
print(type(y))
