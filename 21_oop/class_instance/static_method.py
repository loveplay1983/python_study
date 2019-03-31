class Robot:

    __counter = 0


    def __init__(self):
        type(self).__counter += 1


    # static method, normally its implementation for surface functionality of the class memebers which means it is better to not affect the actual data rather to control or add some sort of functionality for outline computation
    @staticmethod
    def robot_instances():
        return Robot.__counter



if __name__ == '__main__':
    
    print(Robot.robot_instances())
    
    x = Robot()
    print(x.robot_instances())

    y = Robot()
    print(y.robot_instances())

    # Call static method from the class directly
    print(Robot.robot_instances())


