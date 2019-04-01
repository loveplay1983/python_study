class P:

    def __init__(self, first, last):

        self.fn = first
        self.ln = last

    def name(self):
        return self.fn + ' ' + self.ln

class Employee(P):

    def __init__(self, first, last, staffnum):
       
        # super().__init__(first, last)
        P.__init__(self, first, last)
        self.staffnumber = staffnum

    def get_employee(self):
        return self.name() + ' ' + self.staffnumber




