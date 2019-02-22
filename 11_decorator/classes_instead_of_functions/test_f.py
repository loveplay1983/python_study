from callable_for_test_f import A

x = A()
print('Calling the instance')
x(3, 4, x=10, y=11)
print('Call it again')
x(3, 4, x=10, y=11)
