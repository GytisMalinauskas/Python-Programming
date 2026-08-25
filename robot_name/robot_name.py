import random


class Robot:
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        self._name = (random.choice(str.ascii_uppercase) * 2) + str(random.randrange(100, 999, 1))