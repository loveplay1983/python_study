"""
* Class methods are not bound to the instances.
* Class methods are bound to the a class.
"""


class Robot:
    
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    # Class methods are bound to the class itself 
    @classmethod
    def robot_instances(cls):
        return cls, Robot.__counter


if __name__ == '__main__':
    print(Robot.robot_instances())
    x = Robot()
    print(x.robot_instances())

    y = Robot()
    print(y.robot_instances())

    # Call static method from the class directly
    print(Robot.robot_instances())

 



        
