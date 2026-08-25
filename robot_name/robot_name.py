import random
import string

class Robot:
    def __init__(self):
        self._name = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randrange(100, 999, 1))

    @property
    def name(self):
        return self._name

    def reset(self):
        return self._name