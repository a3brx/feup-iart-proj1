from algorithm.mutation import *
from simulation.solution import Solution


class LocalSearch:
    def __init__(self, data):
        self.data = data
        self.solution = Solution.initial(self.data)
        self.iterations = 0
        self.max_iterations = 100

    def get_random_neighbour(self):
        result = self.solution.copy()
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

    def recalculate_attributes(self):
        pass

    def accept_condition(self, delta):
        return delta > 0

    def run(self):
        print("Initial score:", self.solution.get_score())
        while self.iterations < self.max_iterations:
            self.recalculate_attributes()

            neighbour = self.get_random_neighbour()
            delta = neighbour.get_score() - self.solution.get_score()

            if self.accept_condition(delta):
                self.solution = neighbour
                print("-" * 30)
                print("New score:", self.solution.get_score())
                for operation in self.solution.operations:
                    print(operation)
                self.iterations = 0

            self.iterations += 1
