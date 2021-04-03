import copy
import random

import delivery.algorithm.operation.mutation as mutations
from delivery.algorithm.algorithm import Algorithm


class LocalSearch(Algorithm):

    def __init__(self, simulation, max_time=None, max_iterations=5000, max_improveless_iterations=None):
        super().__init__(simulation, max_time, max_iterations,
                         max_improveless_iterations)

        self.mutation_functions = [
            mutations.exchange_positions, mutations.modify_drone]

    def random_neighbour(self, solution):
        solution = copy.deepcopy(solution)

        min_ops = min(1, len(solution) // 1000)
        max_ops = max(1, len(solution) // 150)

        op_count = random.randint(min_ops, max_ops)

        for _ in range(0, op_count):
            mutation_function = random.choice(self.mutation_functions)

            solution = mutation_function(solution, self.simulation)

        return solution
