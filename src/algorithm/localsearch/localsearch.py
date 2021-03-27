from random import choice

from random import choice

from algorithm.mutation import *

class LocalSearch:
    def __init__(self, model):
        self.model = model

    def random_neighbour(self):
        neighbour = self.model.copy()
        functions = [
            insert_operation
        ]
        choice(functions)(neighbour)
        return neighbour

