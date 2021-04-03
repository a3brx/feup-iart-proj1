from math import e
from random import uniform

from delivery.algorithm.localsearch.localsearch import LocalSearch


class SimulatedAnnealing(LocalSearch):
    def __init__(self, data, max_iterations=5000, temperature_schedule=1000, initial_temperature=0.9):
        super().__init__(data, max_iterations)
        self.temperature = initial_temperature
        self.temperature_schedule = temperature_schedule

    def recalculate_attributes(self):
        self.temperature *= self.temperature_schedule

    def accept_condition(self, delta):
        return delta > 0 or (self.temperature > 0 and pow(e, delta / self.temperature) > uniform(0, 1))
