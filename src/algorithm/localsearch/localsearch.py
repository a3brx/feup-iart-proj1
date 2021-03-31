from random import choice, randrange

from algorithm.mutation import *


class LocalSearch:
    def __init__(self, model):
        self.model = model

    def random_neighbour(self, neighbour):
        result = neighbour.copy()
        functions = [
            ("Swap", swap_operations),
            ("Insert", insert_operation),
            ("Remove", remove_operation),
            ("Switch", switch_operation_drone)
        ]
        while True:
            position = randrange(len(functions))
            key, function = functions[position]
            if function(result):
                break
        return result

    def print_solution(self, solution, evaluation):
        for path in solution:
            print(path)
        print("Evaluation:", evaluation)
