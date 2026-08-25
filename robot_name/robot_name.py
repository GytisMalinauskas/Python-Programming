import random
import string

class Robot:
    def __init__(self):
        self._name = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))

    @property
    def name(self):
        return self._name

    def reset(self):
        self._name = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))