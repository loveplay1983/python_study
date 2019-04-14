class MetaCls(type):

    def __new__(cls, clsname, superclasses, attributedict):
        print('class name', clsname)
        print('super classes', superclasses)
        print('attribute dict', attributedict)

        return type.__new__(cls, clsname, superclasses, attributedict)



if __name__ == '__main__':

    class S:
        pass

    class A(S, metaclass=MetaCls):
        pass

    a = A()

