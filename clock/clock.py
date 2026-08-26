"""A module for time representation"""

class Clock:
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{format_hour(self.hour, self.minute):02d}:{format_minute(self.minute):02d}"

    def __eq__(self, other):
        pass

    def __add__(self, minutes):
        total_minutes = self.minute + minutes
        self.hour = format_hour(self.hour, total_minutes)
        self.minute = format_minute(total_minutes)
        return Clock()

    def __sub__(self, minutes):
        total_minutes = self.minute - minutes
        self.hour = format_hour(self.hour, total_minutes)
        self.minute = format_minute(total_minutes)

def format_hour(hour, minute):
    return int((hour + (minute / 60)) % 24)

def format_minute(minute):
    return int(minute % 60)