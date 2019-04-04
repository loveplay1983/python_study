class A:

    def answer(self, *args):

        return 42


class P1(A):
    pass

class P2(A):
    pass

class P3(A):
    pass

if __name__ == '__main__':

    p1 = P1()
    p2 = P2()

    print(p1.answer())
    print(p2.answer())

