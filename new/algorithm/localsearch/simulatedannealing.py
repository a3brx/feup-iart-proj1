from math import e
from random import uniform

from algorithm.localsearch.localsearch import LocalSearch


class SimulatedAnnealing(LocalSearch):
    def __init__(self, data):
        super().__init__(data)
        self.temperature = 1000

    def recalculate_attributes(self):
        self.temperature *= 0.99

    def accept_condition(self, delta):
        return delta > 0 or pow(e, delta / self.temperature) > uniform(0, 1)
