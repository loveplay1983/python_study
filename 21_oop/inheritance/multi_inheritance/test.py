class T:

    def __init__(self):
        pass

    def msg(self):
        print('test message of T')



class TT(T):

    def __init__(self):
        super().__init__()
        pass

    def msg(self):
        print('test message of TT')

t = T()
tt = TT()

t.msg()
tt.msg()

