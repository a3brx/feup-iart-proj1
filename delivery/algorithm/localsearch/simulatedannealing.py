from delivery.algorithm.localsearch.localsearch import LocalSearch

class SimulatedAnnealing(LocalSearch):
    def __init__(self, model):
        super().__init__(model)
