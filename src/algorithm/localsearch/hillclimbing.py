from algorithm.localsearch.localsearch import LocalSearch


class HillClimbing(LocalSearch):
    def __init__(self, model):
        super().__init__(model)

    def run(self):
        neighbour = self.model
        neighbour_evaluation = neighbour.evaluate_solution()
        for path in neighbour.solution:
            print(path)
        print("Evaluation:", neighbour_evaluation)
        it = 0
        while it < 1000:
            new_neighbour = self.random_neighbour(neighbour)
            # print(new_neighbour)
            new_neighbour_evaluation = new_neighbour.evaluate_solution()
            if new_neighbour_evaluation > neighbour_evaluation:
                neighbour = new_neighbour
                neighbour_evaluation = new_neighbour_evaluation
                print("-" * 100)
                for path in neighbour.solution:
                    print(path)
                print("Evaluation:", neighbour_evaluation)
                it = 0
            it += 1
