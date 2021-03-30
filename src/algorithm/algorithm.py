from abc import ABC, abstractmethod
from timeit import default_timer as timer


class Algorithm(ABC):

    def __init__(self, environment, max_time=None, max_iterations=None):
        self.environment = environment
        # TODO missing products, houses and warehouses

        self.starting_time = timer()
        self.iterations = 0

        self.max_time = max_time
        self.max_iterations = max_iterations

    @abstractmethod
    def run(self):
        pass

    def random_solution(self):
        # TODO
        return ["a", "b", "c"]

    def evaluate(self, solution):
        # TODO
        return 10

    def stop(self):
        """Verifies if the algorithm must stop.

        ...
        Returns:
            boolean: True if the algorithm must stop, false otherwise
        """
        return self.max_time is not None and timer() - self.starting_time >= self.max_time \
            or self.max_iterations is not None and self.iterations >= self.max_iterations
