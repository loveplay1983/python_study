from basic_inheritance import *
from overloading_overriding import *

#x = P('John', 'Smith')
#print(x.name())

#y = Employee('Martin', 'Joe', '1001')
#print(y.get_employee())


x = Person('a', 'b')
y = Employee('aa', 'bb', 10)
print(x)
print(y)


i = PersonModified('1', '2', 3)
j = EmployeeModified('11', '22', 3, '1212')
print(i)
print(j)



"""
Traceback (most recent call last):
  File "demo.py", line 18, in <module>
    j = EmployeeModified('11', '22', 3, '1212')
  File "/home/loveplay1983/Workspace/pc_workspace/programming/Python/project/mdn_python_django_as_well_as_python_online_study/python_online_edu/21_oop/inheritance/overloading_overriding.py", line 33, in __init__
    super().__init__(first, last, age)
TypeError: __init__() takes 3 positional arguments but 4 were given

"""
