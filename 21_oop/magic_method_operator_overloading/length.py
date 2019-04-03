class Length:

    __metric = { "mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344 }

    def __init__(self, val, unit='m'):

        self.val = val
        self.unit = unit


    def converse_to_metres(self):

        return self.val * Length.__metric[self.unit]


    def __add__(self, other):

        l = self.converse_to_metres() + other.converse_to_metres()
        # This line of code is used when calling __repr__, since the __repr__ method defines the output form from it.
        #return Length(l / Length.__metric[self.unit], self.unit )
        return l

    def __str__(self):

        return str(self.converse_to_metres())

    def __repr__(self):

        return 'Length(' + str(self.val) + ', "' + self.unit + '")'


