from algorithm.localsearch.localsearch import LocalSearch


class HillClimbing(LocalSearch):
    def __init__(self, model):
        super().__init__(model)

    def run(self):
        # Get first solution
        neighbour = self.model
        neighbour_evaluation = neighbour.evaluate_solution()
        self.print_solution(neighbour.solution, neighbour_evaluation)

        it = 0

        while it < 100:
            new_neighbour = self.random_neighbour(neighbour)
            new_neighbour_evaluation = new_neighbour.evaluate_solution()

            delta = new_neighbour_evaluation - neighbour_evaluation

            if delta > 0:
                neighbour, neighbour_evaluation = new_neighbour, new_neighbour_evaluation
                print("-" * 100)
                self.print_solution(neighbour.solution, neighbour_evaluation)
                it = 0
            
            it += 1
