"""A module for time representation"""

class Clock:
    def __init__(self, hour, minute):
        self.hour = int(hour + (minute / 60))
        self.minute = int(minute % 60)

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour}:{self.minute}"

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass
