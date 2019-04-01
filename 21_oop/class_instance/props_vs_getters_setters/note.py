########################################################
# The following code resides within the builtin.py file#
########################################################
#class property(object):
#    """
#    property(fget=None, fset=None, fdel=None, doc=None) -> property attribute
#
#    fget is a function to be used for getting an attribute value, and likewise
#    fset is a function for setting, and fdel a function for del'ing, an
#    attribute.  Typical use is to define a managed attribute x:
#
#    class C(object):
#        def getx(self): return self._x
#        def setx(self, value): self._x = value
#        def delx(self): del self._x
#        x = property(getx, setx, delx, "I'm the 'x' property.")
#
#    Decorators make defining new properties or modifying existing ones easy:
#
#    class C(object):
#        @property
#        def x(self):
#            "I am the 'x' property."
#            return self._x
#        @x.setter
#        def x(self, value):
#            self._x = value
#        @x.deleter
#        def x(self):
#            del self._x
#    """
class C:
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x

    x = property(getx, setx, delx, "I'm the 'x' property.")

