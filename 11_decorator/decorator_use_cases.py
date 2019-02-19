############# helper function####################
def nl():
    print('\n')

##################################################

# Checking args with decorator
def arg_check(f):
    def test(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception('Input is not Integer.')
    return test


@arg_check
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1, 10):
    print(i, '- ', factorial(i))


# print(factorial(-1))

nl()

# Couting function calls with decorators
def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0
    return helper

@call_counter
def my_func(x):
    return x + 1

#print(my_func.calls)

#for i in range(10):
#    my_func(i)

#print(my_func.calls)


# With arbitrary args
def call_counter(func):
    def helper(*args, **kwargs):
        helper.calls += 1
        return func(*args, **kwargs)
    helper.calls = 0
    return helper

@call_counter
def my_func(x):
    return x + 1

@call_counter
def my_func2(x, y=1):
    return x*y + 1

print('my_func has been called ' + str(my_func.calls) + ' times')

for i in range(10):
    my_func(i)

my_func2(1,2)
my_func2(1,2)
my_func2(1,2)
print('my_func has been called ' + str(my_func.calls) + ' times')
print('my_func2 has been called ' + str(my_func2.calls) + ' times')

nl()

# Decorator with parameters
def evening_greeting(func):
    def function_wrapper(x):
        print('Good evening, ' + func.__name__ + ' returns')
        func(x)
    return function_wrapper

def morning_greeting(func):
    def function_wrapper(x):
        print('Morning ' + func.__name_+ ' returns')
    return function_wrapper

@evening_greeting
def foo(x):
    print(42)

foo('Hi')

# The above code is "hard-coded" in which the "greeting" content cannot
# be changed forever where we need to input arbitrary content

def greeting(content):                 # The decorator now has a parameter
    def greeting_dec(func):            # Add another layer outside the wrapper
        def func_wrapper(x):           # Wrapper function
            print(content + ', ' + func.__name__ + ' returns')
            func(x)                    # The function which will be decorated (it runs itself method)
        return func_wrapper
    return greeting_dec

@greeting('Hail')
def foo(x):
    print(x + ' function foo prints this line')

foo('Hello world')

