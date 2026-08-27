"""A module for time representation"""

class Clock:
    def __init__(self, hour, minute):
        total_minutes = hour * 60 + minute
        self.day = format_day(total_minutes)
        self.hour = format_hour(total_minutes)
        self.minute = format_minute(total_minutes)

    def __repr__(self):
        return f"Clock({self.hour}, {self.minute})"

    def __str__(self):
        return f"{self.hour:02d}:{self.minute:02d}"

    def __eq__(self, other):
        return self.hour == other.hour and self.minute == other.minute and self.day == other.day

    def __add__(self, minutes):
        total_minutes = self.minute + minutes + (self.hour * 60) + self.day * 1440
        self.hour = format_hour(total_minutes)
        self.minute = format_minute(total_minutes)
        self.day = format_day(total_minutes)
        return Clock(self.hour, self.minute)

    def __sub__(self, minutes):
        total_minutes = self.minute - minutes + (self.hour * 60) + self.day * 1440
        self.hour = format_hour(total_minutes)
        self.minute = format_minute(total_minutes)
        self.day = format_day(total_minutes)
        return Clock(self.hour, self.minute)

def format_day(minute: int):
    """formats days"""
    return int(minute / 1440)

def format_hour(minute: int):
    """formats hours"""
    return int(minute % 1440 / 60 % 24)

def format_minute(minute: int):
    """formats minutes"""
    return int(minute % 1440 % 60)