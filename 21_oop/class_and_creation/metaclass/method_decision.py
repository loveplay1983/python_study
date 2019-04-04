## the following variable would be set as the result of a runtime calculation:
#x = input("Do you need the answer? (y/n): ")
#if x=="y":
#    required = True
#else:
#    required = False
#
#def the_answer(self, *args):
#        return 42
#
#class Philosopher1:
#    pass
#if required:
#    # Notice that Philosopher1.the_answer and the_answer both of which are function name without parentheses
#    Philosopher1.the_answer = the_answer
#
#class Philosopher2:
#    pass
#if required:
#    Philosopher2.the_answer = the_answer
#
#class Philosopher3:
#    pass
#if required:
#    Philosopher3.the_answer = the_answer
#
#plato = Philosopher1()
#kant = Philosopher2()
## let's see what Plato and Kant have to say :-)
#if required:
#
#    # Notice that when calling the_answer method from the instance of Philosopher, the trailing part is added by the parentheses
#    print(kant.the_answer())
#    print(plato.the_answer())
#else:
#    print("The silence of the philosphers")
#
#

"""
Even though this is another solution to our problem, there are still some serious drawbacks. It's error-prone, because we have to add the same code to every class and it seems likely that we might forget it. Besides this it's getting hardly manageable and maybe even confusing, if there are many methods we want to add.

We can improve our approach by defining a manager function and avoiding redundant code this way. The manager function will be used to augment the classes conditionally.
"""

#x = input('y/n')
#if x == 'y':
#    required = True
#
#else:
#    required = False
#
#
#def answer(self, *args):
#    return 42
#
## Manager function
#def augment_answer(cls):                 # cls stands for the class name to which we pass into the manager function
#    if required:
#        cls.answer = answer
#
#class P1:
#    pass
#augment_answer(P1)
#
#class P2:
#    pass
#augment_answer(P1)
#
#class P3:
#    pass
#augment_answer(P1)
#
#p1 = P1()
#p2 = P2()
#p3 = P3()
#
#if required:
#    print(p1.answer())
#    print(p2.answer())
#    print(p3.answer())
#else:
#    print('The silence person.')
#
"""
This is again useful to solve our problem, but we, i.e. the class designers, must be careful not to forget to call the manager function "augment_answer". The code should be executed automatically. We need a way to make sure that "some" code might be executed automatically after the end of a class definition.
"""

x = input("Do you need the answer? (y/n): ")
if x=="y":
    required = True
else:
    required = False


def the_answer(self, *args):
        return 42

def augment_answer(cls):
    if required:
        cls.the_answer = the_answer
    # we have to return the class now:
    return cls


@augment_answer
class Philosopher1:
    pass
@augment_answer
class Philosopher2:
    pass
@augment_answer
class Philosopher3:
    pass


plato = Philosopher1()
kant = Philosopher2()


# let's see what Plato and Kant have to say :-)
if required:
    print(kant.the_answer())
    print(plato.the_answer())
else:
    print("The silence of the philosphers")


