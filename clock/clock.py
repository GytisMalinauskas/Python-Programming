"""A module for time representation"""

class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        pass

    def __str__(self):
        return f"{self.hour}:{self.minute}"

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass
