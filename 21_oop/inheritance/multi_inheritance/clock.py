"""
class SubclassName(BaseClass1, BaseClass2, BaseClass3, ...):
    pass

"""

# Clock class example with redundant code

#def __init__(self,hours=0, minutes=0, seconds=0):
#        self._hours = hours
#        self.__minutes = minutes
#        self.__seconds = seconds
#
#    def set(self,hours, minutes, seconds=0):
#        self._hours = hours
#        self.__minutes = minutes
#        self.__seconds = seconds


# Complete clock class with proper definition

class Clock:

    """
    Clock simulation of 24 hours clock
    """

    def __init__(self, hours, minutes, seconds):

        """
        Parameters hours, minutes and seconds must be integers and satisfy 
        the following equations
        0 <= h < 24
        0 <= m < 60
        0 <= s < 60
        """
        self.set_clock(hours, minutes, seconds)

    def set_clock(self, hours, minutes, seconds):

        if type(hours) == int and 0 <= hours and hours < 24:
            self.__hours = hours
        else:
            raise TypeError('Hours must be integer value between 0 to 23 per day!')

        if type(minutes) == int and 0 <= 60 and minutes < 60:
            self.__minutes = minutes
        else:
            raise TypeError('Minutes must be integer value between 0 to 59 per hour!')

        if type(seconds) == int and 0 <= 60 and seconds < 60:
            self.__seconds = seconds
        else:
            raise TypeError('Seconds must be integer value between 0 to 59 per minute!')

    
    def __str__(self):
        # for Python format syntax:
        # "{0:02d} {1:02d} {2:02d}". format(0,1,2)
        # :02d stands for the result in which it takes up to 2 decimal value(base 10)
        return "{0:02d} - {1:02d} - {2:02d}".format(self.__hours, self.__minutes, self.__seconds)

    
    def tick(self):
        """
        This method let clock "tick" which means the internal time will be advanced each one second.
        """

        if self.__seconds == 59:
            self.__seconds = 0
            if self.__minutes == 59:
                self.__minutes = 0
                if self.__hours == 23:
                    self.__hours = 0
                else:
                    self.__hours += 1
            else:
                self.__minutes += 1
        else:
            self.__seconds += 1



