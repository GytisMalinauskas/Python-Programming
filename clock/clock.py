"""A module for time representation"""

class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{format_hour(self.hour, self.minute):.2f}:{format_minute(self.minute)}"

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        pass

    def __sub__(self, minutes):
        pass

def format_hour(hour, minute):
    return int(hour + (minute / 60))

def format_minute(minute):
    return int(minute % 60)