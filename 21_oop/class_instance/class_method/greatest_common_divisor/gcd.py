class Fraction:

    def __init__(self, n, d):
        """
        Return numerator and denominator when initializing the 
        Fraction class.

        Because reduce is a classmethod so class Fraction.reduce(x, y).

        The class method reduce calls static method gcd since the static method is not bound to the class instance 
        and the class method its first argument is cls which stands for the class itself, so we can call the cls.gcd()
        """
        self.numerator, self.denominator = Fraction.reduce(n, d)


    @staticmethod
    def gcd(a, b):
        while b != 0:
            a , b = b, a%b
        return a


    @classmethod
    def reduce(cls, n1, n2):
        g = cls.gcd(n1, n2)
        return (n1 // g, n2 // g)

    def __str__(self):
        return str(self.numerator) + '/' + str(self.denominator)


