import random
import string

class Robot:
    def __init__(self):
        self._name = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
        self.used_names = []
    @property
    def name(self):
        return self._name

    def reset(self):
        self.used_names.append(self._name)
        self._name = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))
        if self._name in self.used_names:
            self._name = self._name = random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))