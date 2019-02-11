"""
A variable can't be both local and global inside of a function. So Python decides that we want a local variable due to the assignment to s inside of f(), so the first print statement before the definition of s throws the error message above. Any variable which is changed or created inside of a function is local, if it hasn't been declared as a global variable. To tell Python, that we want to use the global variable, we have to explicitly state this by using the
keyword "global".
"""

def f():
    """
    Define a global variable by keyword 'global',
    and test it inside and outside of function body.
    """
    global dynamic_var
    print(dynamic_var)
    dynamic_var = 'hello world, I am global variable call which is inside...'
    print(dynamic_var)

dynamic_var = 'hello world, I am global variable call which is outside.'

f()
# dynamic_var was defined as global and assigned outside of function body
# so the value of dynamic_var is now changed to 'hello workd, this is...'
print(dynamic_var)

# local variable cannot be accessed from outside when the function call is done.
def f():
    """
    Define local variable and tet it inside and outside of func body
    """

    local_var = 'hello world, I am a local var.'
    print(local_var)

f()
# print(local_var)            # error raised since the local var can only be access within the function body.

# NameError: name 'local_var' is not defined


print('\n' * 5)


# Global var in nested function body
# global var only take effect within global scope
# which means you can only assign the value to local or global scope
# specifically, otherwise it will be endedup with only work for either
# local or global
def f():
    """
    Test for nested function and global variable
    """

    a = 42
    def g():
        global a
        a = 1
    print('Before calling g: ' + str(a))
    print('Callingg now: ')
    g()
    print('After calling g: ' + str(a))

f()
print('a in main: ' + str(a))

print('\n' * 5)
# Nonlocal variable
# It is not possible to change variable in module scope for nonlocal var
# "module scope", for example, inside of a function body

def f():
    global x
    print(x)
x = 3
f()

#def f():
#    """
#    Using nonlocal instead of global keywrod
#    """
#    nonlocal x
#    print(x)
#
#x = 3
#f()
#
# SyntaxError: no binding for nonlocal 'x' found
"""
Nonlocal bindings can only be used inside of nested functions. A nonlocal variable has to be defined in the enclosing function scope. If the variable is not defined in the enclosing function scope,i.e. in a global scope for example,  the variable cannot be defined in the nested scope. This is another difference to the "global" semantics.
"""

print('\n'*5)

def f():
    x = 33
    def g():
        nonlocal x
        x = 44
    print('Before calling g: ' + str(x))
    print('About to call g()')
    g()
    print('After calling g: ' + str(x))

x = 3
f()
print('x in main: ' + str(x))

################ Summary #############################
"""
1. There are global, local and nonlocal;

2. Global works for the data that if there isn't any otherthan global defintion, so therefore if there is variable only defined by global keyword, it works for both local or gloal, but nested function body;

3. Nonlocal works for nested function body only and only if the variable is
pre-defined which means you have to define the variable that you want to put it on nonlocal before you put nonlocal on it;

4. Finally, to sum all up:
   a. Use local variable within the function body;
   b. Use nonlocal within nested function body;
   c. Use global in the outside world of local and nonlocal if you want to use local and nonlocal, otherwise, it will work for all scope.
"""
