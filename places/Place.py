from math import sqrt

class Place:
    def __init__(self, x, y):
        self.location = [x, y]

    def distance(self, operand):
        return sqrt((self.location[0] - operand.location[0]) ** 2 + (self.location[1] - operand.location[1]) ** 2)