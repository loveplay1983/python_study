"""
Combine clock and calendar classes.
"""

from clock import Clock
from calendar import Calendar


class clockCalendar(Clock, Calendar):

    """
    This class implements a clock with integrated calendar which is a case of multi-inheritance.
    """

    def __init__(self, day, month, year, hour, minute, second):

        Clock.__init__(self, hour, minute, second)
        Calendar.__init__(self, day, month, year)


    def tick(self):

        """
        Advance the clock by one second.
        """

        previous_hour = self.__hours
        Clock.tick(self)
        if (self.__hours < previous_hour):
            self.advance()



    def __str__(self):
        
        return Calendar.__str__(self) + ', ' + Clock.__str__(self)



