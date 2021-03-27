from algorithm.localsearch.localsearch import LocalSearch


class HillClimbing(LocalSearch):
    def __init__(self, model):
        super().__init__(model)

    def run(self):
        neighbour = self.model
        it = 0
        while it < 10:
            new_neighbour = self.random_neighbour(neighbour)
            # print(new_neighbour)
            if new_neighbour.evaluate_solution() > neighbour.evaluate_solution():
                neighbour = new_neighbour
                print("-" * 100)
                for path in neighbour.solution:
                    print(path)
                it = 0
            it += 1
