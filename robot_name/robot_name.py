
"""A module for Robot name generation"""
import random
import string

names_in_use = []

class Robot:
    """Initializes robot with a random generated name"""
    def __init__(self):
        self._name = generate_name()
        names_in_use.append(self._name)
        
    @property
    def name(self):
        """Returns name value"""
        return self._name

    def reset(self):
        """Resets name value"""
        while self._name in self.used_names:
            self._name = generate_name()
        names_in_use.append(self._name)
    
def generate_name():
    """Generates robot name"""
    return random.choice(string.ascii_uppercase) + random.choice(string.ascii_uppercase) + str(random.randrange(10)) + str(random.randrange(10)) + str(random.randrange(10))