import random
import string

class Robot:
    def __init__(self):
        self._name = ""

    @property
    def name(self):
        self._name = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randrange(100, 999, 1))
        return self._name

    def reset(self):
        self._name = ""
        self.name