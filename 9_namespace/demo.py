"""
global names of a module
local names in a function or method invocation
built-in names: this namespace contains built-in fuctions (e.g. abs(), cmp(), ...) and built-in exception names

A scope refers to a region of a program where a namespace can be directly accessed, i.e. without using a namespace prefix. In other words: The scope of a name is the area of a program where this name can be unambiguously used, for example, inside of a function. A name's namespace is identical to it's scope. Scopes are defined statically, but they are used dynamically.
During program execution there are the following nested scopes available:

    the innermost scope is searched first and it contains the local names
    the scopes of any enclosing functions, which are searched starting with the nearest enclosing scope
    the next-to-last scope contains the current module's global names
    the outermost scope, which is searched last, is the namespace containing the built-in names 

"""


