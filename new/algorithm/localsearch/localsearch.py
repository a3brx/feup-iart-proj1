from algorithm.mutation import *
from solution.solution import Solution


class LocalSearch:
    def __init__(self, data):
        self.data = data
        self.solution = Solution.initial(self.data)
        self.solution.get_score()
        self.iterations = 0
        self.max_iterations = 100

    def get_random_neighbour(self):
        result = self.solution.copy()
        functions = [
            ("Position", swap_operations),
            ("Drone", switch_operation_drone),
            ("Order", swap_order_items)
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

    def print_solution(self, text="new"):
        print(text + " score:", self.solution.get_score())
        #for operation in self.solution.operations:
        #    print(operation)
        print("-" * 60)

    def run(self):
        self.print_solution("initial")

        while self.iterations < self.max_iterations:
            self.recalculate_attributes()

            neighbour = self.get_random_neighbour()
            delta = neighbour.get_score() - self.solution.get_score()

            if self.accept_condition(delta):
                self.solution = neighbour
                self.print_solution()
                self.iterations = 0

            self.iterations += 1
