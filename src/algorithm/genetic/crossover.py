from abc import ABC, abstractmethod
import copy


class Crossover(ABC):

    @abstractmethod
    def run(self, parent1, parent2):
        pass


class OnePointCrossover(Crossover):

    def run(self, parent1, parent2):
        # TODO
        return copy.deepcopy(parent1)


class OrderCrossover(Crossover):

    def run(self, parent1, parent2):
        # TODO
        return copy.deepcopy(parent1)