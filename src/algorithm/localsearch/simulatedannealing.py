from math import e
from random import random

from algorithm.localsearch.localsearch import LocalSearch


class SimulatedAnnealing(LocalSearch):
    def __init__(self, model):
        super().__init__(model)
        self.reset_temperature()

    def reset_temperature(self):
        self.temperature = 1000

    def schedule(self):
        self.temperature *= 0.9

    def accept_function(self, delta):
        return delta > 0 or (delta < 0 and e ** (delta / self.temperature) > random())

    def run(self):
        # Get first solution
        neighbour = self.model
        neighbour_evaluation = neighbour.evaluate_solution()
        self.print_solution(neighbour.solution, neighbour_evaluation)

        self.reset_temperature()
        it = 0

        while it < 100:
            self.schedule()
            new_neighbour = self.random_neighbour(neighbour)
            new_neighbour_evaluation = new_neighbour.evaluate_solution()

            delta = new_neighbour_evaluation - neighbour_evaluation

            if self.accept_function(delta):
                neighbour, neighbour_evaluation = new_neighbour, new_neighbour_evaluation
                print("-" * 100)
                self.print_solution(neighbour.solution, neighbour_evaluation)
                it = 0

            it += 1
