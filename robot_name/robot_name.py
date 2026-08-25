import random

class Robot:
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        self.name = str(random.randrange(100, 999, 1))