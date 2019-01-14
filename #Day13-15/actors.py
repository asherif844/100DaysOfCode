import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def defensive_role(self):
        role = random.randit(1, 12)
        return role * self.level
