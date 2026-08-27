"""A module for time representation"""

class Clock:
    def __init__(self, hour, minute):
        self.day = 0
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{format_hour(self.hour, self.minute):02d}:{format_minute(self.minute):02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute

    def __add__(self, minutes):
        total_minutes = self.minute + minutes
        self.hour = format_hour(self.hour, total_minutes)
        self.minute = format_minute(total_minutes)
        return Clock(self.hour, self.minute)

    def __sub__(self, minutes):
        total_minutes = self.minute - minutes
        self.hour = format_hour(self.hour, total_minutes)
        self.minute = format_minute(total_minutes)
        return Clock(self.hour, self.minute)


def format_hour(hour, minute):
    """formats hours"""
    return int((hour + (minute / 60)) % 24)

def format_minute(minute):
    """formats minutes"""
    return int(minute % 60)