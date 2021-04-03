from delivery.algorithm.localsearch.localsearch import LocalSearch


class HillClimbing(LocalSearch):

    def __init__(self, simulation, max_time=None, max_iterations=5000, max_improveless_iterations=None):
        super().__init__(simulation, max_time, max_iterations,
                         max_improveless_iterations)

    def random_better_neighbour(self, solution, max_iteration_search=500):
        initial_score = self.evaluate(solution)

        for _ in range(0, max_iteration_search):
            neighbour = self.random_neighbour(solution)

            neighbour_score = self.evaluate(neighbour)

            print(f'Neighbour: {neighbour_score}')

            if neighbour_score > initial_score:
                return (neighbour, neighbour_score)

        return (solution, initial_score)

    def run(self):
        solution = self.random_solution()
        score = self.evaluate(solution)

        print(score)

        while not self.stop():
            self.iterations += 1

            neighbour, neighbour_score = self.random_better_neighbour(solution)

            if neighbour_score > score:
                print(f'Improved from {score} to {neighbour_score}')
                solution = neighbour
                score = neighbour_score
            else:
                return solution

        return solution
