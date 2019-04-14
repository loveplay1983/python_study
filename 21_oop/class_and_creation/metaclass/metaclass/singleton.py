class Singleton(type):
    """
    This class does following things:

    1. Making a metaclass which inherited from type

    2. Whichever subclass who is inherited from or using `metaclass=xyz` argument will be affectd from this metaclass.

        a. The metaclass has a hidden class attribute which is `_instances` dict, for it we should not modify or change
        it since there is a `_` sign right before.

        b. Define __call__ for metaclass, when metaclass is called, the method body is triggered automatically.

        c. Determine whether _instances dict is empty, return super class `type` its __call__ method.

        d. For all the works has been done above, we therefore can initialize our own class which has inherited from this
        metaclass from the same superclass, i.e. it is a singleton class which means it is always initialized from the same
        class `type`.

    """


    _instances = {}

    def __call__(cls, *args, **kwargs):                                                # Making this Singleton class a callable object

        if cls not in cls._instances:

            """
            super([type[, object-or-type]])
            Return a proxy object that delegates method calls to a parent or sibling class of type.
            This is useful for accessing inherited methods that have been overridden in a class.
            The search order is same as that used by getattr() except that the type itself is skipped.
            """
            # super().__call__(*args, **kwargs) does same thing
            # super(classname, self).__call__(...)
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)      # Calling superclass its __call__ method
            return cls._instances[cls]



