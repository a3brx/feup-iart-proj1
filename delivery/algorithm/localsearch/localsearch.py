from timeit import default_timer as timer

from delivery.algorithm.operation.neighbourhood import *
from delivery.solution.solution import Solution


class LocalSearch:

    ITERATIONS_PER_RESULT = 10

    def __init__(self, data, max_iterations=5000, iteration_search=50, save_results=False):
        self.data = data
        self.solution = Solution.initial(self.data)
        self.solution.get_score()
        self.iterations = 0
        self.max_iterations = max_iterations
        self.save_results = save_results
        self.iteration_search = iteration_search
        if self.save_results:
            self.results_file = open(
                f'results_{str(timer())}.log', 'a')
            self.results_file.write(self.output_legend() + "\n")

    def get_random_neighbour(self):
        functions = [
            ("Position", swap_operations),
            ("Drone", switch_operation_drone),
            ("Order", swap_order_items)
        ]
        max_result = self.solution.copy()
        max_score = max_result.get_score()
        for _ in range(self.iteration_search):
            new_result = self.solution.copy()
            position = randrange(len(functions))
            key, function = functions[position]
            if function(new_result):
                new_score = new_result.get_score()
                if new_score > max_score:
                    max_result, max_score = new_result, new_score
        return max_result

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
        self.solution = solution

    def output_legend(self):
        return "Iteration;Score"

    def output_line(self):
        return str(self.total_iterations) + ";" + str(self.solution.get_score())

    def run(self):
        print("Starting search")
        print("Iteration 0 with initial solution of", self.solution.get_score())

        for self.total_iterations in range(1, self.max_iterations + 1):
            self.recalculate_attributes()

            neighbour = self.get_random_neighbour()
            delta = neighbour.get_score() - self.solution.get_score()

            if self.accept_condition(delta):
                self.set_solution(neighbour)
                print("Iteration", self.total_iterations,
                      "with new solution of", self.solution.get_score())

            if self.total_iterations % LocalSearch.ITERATIONS_PER_RESULT == 0:
                self.results_file.write(self.output_line() + "\n")

        return self.solution
