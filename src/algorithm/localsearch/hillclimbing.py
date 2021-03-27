from algorithm.localsearch.localsearch import LocalSearch


class HillClimbing(LocalSearch):
    def __init__(self, model):
        super().__init__(model)

    def run(self):
        neighbour = self.model
        it = 0
        while it < 3:
            new_neighbour = self.random_neighbour(neighbour)
            print("-" * 100)
            for path in new_neighbour.solution:
                print(path)
            it += 1
