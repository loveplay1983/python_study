"""
The term "memoization" was introduced by Donald Michie in the year 1968. It's based on the Latin word memorandum, meaning "to be remembered". It's not a misspelling of the word memorization, though in a way it has something in common. Memoisation is a technique used in computing to speed up programs. This is accomplished by memorizing the calculation results of processed input such as the results of function calls. If the same input or a function call with the same parameters is
used, the previously stored results can be used again and unnecessary calculation are avoided. In many cases a simple array is used for storing the results, but lots of other structures can be used as well, such as associative arrays, called hashes in Perl or dictionaries in Python.

Memoization can be explicitly programmed by the programmer, but some programming languages like Python provide mechanisms to automatically memoize functions.
"""

"""
We define and use a function which we call memoize. memoize() takes a function as an argument. The function memoize uses a dictionary "memo" to store the function results. Though the variable "memo" as well as the function "f" are local to memoize, they are captured by a closure through the helper function which is returned as a reference by memoize(). So, the call memoize(fib) returns a reference to the helper() which is doing what fib() would do on its own plus a wrapper which saves the
calculated results. For an integer 'n' fib(n) will only be called, if n is not in the memo dictionary. If it is in it, we can output memo[n] as the result of fib(n).
"""

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

@memoize
def fib(n):
    if n==0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(2))
