from delivery.algorithm.operation.neighbourhood import *
from delivery.solution.solution import Solution


class LocalSearch:
    def __init__(self, data, max_iterations):
        self.data = data
        self.solution = Solution.initial(self.data)
        self.solution.get_score()
        self.iterations = 0
        self.max_iterations = max_iterations
        self.solution_list = [(0, self.solution)]

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
        pass
        # print(text + " score:", self.solution.get_score())
        # for operation in self.solution.operations:
        #    print(operation)
        # print("-" * 60)

    def set_solution(self, solution):
        if solution.get_score() != self.solution.get_score():
            print("score:", self.solution.get_score())
            self.solution_list.append((self.total_iterations, solution))
        self.solution = solution

    def run(self):
        for self.total_iterations in range(1, self.max_iterations + 1):
            self.recalculate_attributes()

            neighbour = self.get_random_neighbour()
            delta = neighbour.get_score() - self.solution.get_score()

            if self.accept_condition(delta):
                self.set_solution(neighbour)

            if self.iterations > self.max_iterations:
                break

        self.solution_list.append((self.max_iterations, self.solution))
        return self.solution
