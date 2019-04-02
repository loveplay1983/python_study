"""
This class implements a calendar.
"""

class Calendar:

    months = (31,28,31,30,31,30,31,31,30,31,30,31)
    date_style = 'British'

    @staticmethod
    def leapyear(year):
        """
        This method returns True if the parameter year is a leap year, False othewise.
        """


        if not year % 4 == 0:
            return False
        elif not year % 100 == 0:
            return False
        elif not year % 400 == 0:
            return False
        else:
            return True


    def __init__(self, d, m, y):

        """
        d, m, y have to be integer values and year has to be a four digit year number.
        """

        self.set_calendar(d, m, y)

    def set_calendar(self, d, m, y):

        if type(d) == int and type(m) == int and type(y) == int:
            self.__days = d
            self.__months = m
            self.__years = y

        else:
            raise TypeError('d, m, y have to be integers!')

    def __str__(self):
        
        if Calendar.data_style == 'British':
            return '{0:02d} / {1:02d} / {2:04d}'.format(self.__days,
                                                        self.__months,
                                                        self.__years)
        else:
            # calendar style other than british 
            return '{0:02d} / {1:02d} / {2:04d}'.format(self.__days,
                                                        self.__months,
                                                        self.__years)
        
    def advance(self):

        """
        This method advances to the next day.
        """

        max_days = Calendar.months[self.__months - 1]
        if self.__months == 2 and Calendar.leapyear(self.__years):
            max_days += 1
        if self.__days == max_days:
            self.__days = 1
            if self.__months == 12:
                self.__months = 1
                self.__years += 1
            else:
                self.__months += 1
        else:
            self.__days += 1





