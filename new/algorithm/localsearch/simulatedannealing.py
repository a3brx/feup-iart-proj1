from math import e
from random import uniform

from algorithm.localsearch.localsearch import LocalSearch


class SimulatedAnnealing(LocalSearch):
    def __init__(self, data, max_iterations, initial_temperature, annealing_factor):
        super().__init__(data, max_iterations)
        self.temperature = initial_temperature
        self.annealing_factor = annealing_factor

    def recalculate_attributes(self):
        self.temperature *= self.annealing_factor

    def accept_condition(self, delta):
        return delta > 0 or (self.temperature > 0 and pow(e, delta / self.temperature) > uniform(0, 1))
