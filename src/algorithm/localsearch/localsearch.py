from random import choice

from random import choice

from algorithm.mutation import *

class LocalSearch:
    def __init__(self, model):
        self.model = model

    def random_neighbour(self, neighbour):
        result = neighbour.copy()
        functions = [
            swap_operations,
            insert_operation,
            remove_operation,
            switch_operation_drone
        ]
        choice(functions)(result)
        return result

