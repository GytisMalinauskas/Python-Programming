"""A module for time representation"""

class Clock:
    def __init__(self, hour, minute):
        self.day = 0
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{format_hour(self.hour * 60 + self.minute):02d}:{format_minute(self.hour * 60 + self.minute):02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute and self.day == other.day

    def __add__(self, minutes):
        total_minutes = self.minute + minutes + (self.hour * 60) + self.day * 24 * 60
        self.hour = format_hour(total_minutes)
        self.minute = format_minute(total_minutes)
        self.day = ...
        return Clock(self.hour, self.minute)

    def __sub__(self, minutes):
        total_minutes = self.minute - minutes + (self.hour * 60) + self.day * 24 * 60
        self.hour = format_hour(total_minutes)
        self.minute = format_minute(total_minutes)
        self.day = ...
        return Clock(self.hour, self.minute)

def format_day(minute: int):
    """formats days"""
    return int(minute / 1440)

def format_hour(minute: int):
    """formats hours"""
    return int(minute % 1440 % 24)

def format_minute(minute: int):
    """formats minutes"""
    return int(minute % 60)