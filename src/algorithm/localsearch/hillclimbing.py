from algorithm.localsearch.localsearch import LocalSearch

class HillClimbing(LocalSearch):
    def __init__(self, model):
        super().__init__(model)

    def run(self):
        self.insert_operation()