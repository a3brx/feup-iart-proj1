from math import e
from random import uniform

from delivery.algorithm.localsearch.localsearch import LocalSearch


class SimulatedAnnealing(LocalSearch):
    def __init__(self, data, max_iterations=5000, iteration_search=50, save_results=False, temperature_schedule=0.9, initial_temperature=1000):
        super().__init__(data, max_iterations, iteration_search, save_results)
        self.temperature = initial_temperature
        self.temperature_schedule = temperature_schedule

    def recalculate_attributes(self):
        self.temperature *= self.temperature_schedule

    def accept_condition(self, delta):
        return delta > 0 or (self.temperature > 0 and pow(e, delta / self.temperature) > uniform(0, 1))
    
    def output_legend(self):
        return "Iteration;Score;Temperature"

    def output_line(self):
        return str(self.total_iterations) + ";" + str(self.solution.get_score()) + ";" + str(self.temperature)
