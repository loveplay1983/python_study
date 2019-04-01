from robot_law import Robot

# Class attributes vs instance attributes

# Both class and its instance can have their onw attributes, thus, the class attributes are shared by all the instances
# Where the instance attributes are quite closely bound to the instances themselves.

class A:
    a = 'class attr'

    pass


x = A()
y = A()

x.aa = 'instance attr'
A.a = 'hello world'




if __name__ == '__main__':

    # print(x.a == y.a)
    # print(x.a == y.a)
    print('Instance attr: ' + x.aa)
    print('Class attr: ' + A.a)
    print('Class attr: ' + x.a)
    print('Class attr: ' + y.a)
 
 
    # __dict__ for class or object attr
    print(A.__dict__)
    print(x.__dict__)
    print(y.__dict__)
 
######################### Robot laws #########################################################
    for number, text in enumerate(Robot.three_laws):
        print(str(number+1) + " - " +  text)
