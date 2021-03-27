from algorithm.localsearch.localsearch import LocalSearch

class HillClimbing(LocalSearch):
    def __init__(self, model):
        super().__init__(model)

    def run(self):
        for _ in range(10):
            neighbour = self.random_neighbour()
            print("-" * 100)
            for path in neighbour.solution:
                print(path)