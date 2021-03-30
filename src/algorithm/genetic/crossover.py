"""Holds crossover classes used in genetic algorithms.

Classes:

    Crossover
    OnePointCrossover
    OrderCrossover
"""

from abc import ABC, abstractmethod
import copy
import random

from algorithm.genetic import chromosome


class Crossover(ABC):
    """The general abstract crossover class.

    Crossover, also called recombination, is a genetic operator used to combine the genetic information of two parents
    to generate new offspring. It is one way to stochastically generate new solutions from an existing population, and
    is analogous to the crossover that happens during sexual reproduction in biology. Solutions can also be generated
    by cloning an existing solution, which is analogous to asexual reproduction. Newly generated solutions are
    typically mutated before being added to the population.

    Being an abstract class, works as an interface in the sense that it obliges all crossovers to implement a run
    method.
    """

    @abstractmethod
    def run(self, parent1, parent2):
        """Runs the crossover.

        Since it is an abstract method, the arguments are not required, but are present to assert a sort of convention,
        this is, every crossover function should receive this arguments to run properly.

        ...
        Args:
            parent1 (List[Path]): The first parent chromosome
            parent2 (List[Path]): The second parent chromosome

        Returns:
            (List[Path], List[Path]): The generated offsprings
        """
        pass


class OnePointCrossover(Crossover):
    """For each offspring, gets the first genes of a parent and the rest of the genes from the other parent.

    Given two parents, a random cut point is selected in the same place for both. The left part is taken from the
    first parent, completing the rest with non repeated genes from the second parent. Vice versa for a second offspring.
    """

    def run(self, parent1, parent2):
        """Runs the one point crossover.

        ...
        Args:
            parent1 (List[Path]): The solution of the first parent
            parent2 (List[Path]): The solution of the second parent

        Returns:
            (List[Path], List[Path]): The two generated offsprings
        """
        # generates the cut point
        min_size = min(len(parent1), len(parent2))
        cut_point = random.randint(1, min_size - 1)

        # starts the offsprings with the first part of the parents
        offspring1 = []
        offspring2 = []
        for idx in range(cut_point):
            offspring1.append(copy.deepcopy(parent1[idx]))
            offspring2.append(copy.deepcopy(parent2[idx]))

        # finishes the building of the offspring with the other parent
        for gene in parent2:
            if chromosome.valid_append(offspring1, gene):
                offspring1.append(copy.deepcopy(gene))
        for gene in parent1:
            if chromosome.valid_append(offspring2, gene):
                offspring2.append(copy.deepcopy(gene))

        return (offspring1, offspring2)


class OrderCrossover(Crossover):
    """For each offspring, gets a sequence of genes from the middle of a parent and the rest from the other parent.

    Builds offspring by choosing a subtour (between two random cut points) of a parent and preserving the relative order
    of bits of the other parent. Vice versa for a second offspring.
    """

    def run(self, parent1, parent2):
        """Runs the order crossover.

        ...
        Args:
            parent1 (List[Path]): The solution of the first parent
            parent2 (List[Path]): The solution of the second parent

        Returns:
            (List[Path], List[Path]): The two generated offsprings
        """
        # generates the cut points
        min_size = min(len(parent1), len(parent2))
        [p1, p2] = random.sample(range(1, min_size - 1), 2)

        # starts the offsprings with the sequence between the points in the parents
        offspring1 = []
        offspring2 = []
        for idx in range(p1, p2):
            offspring1.append(copy.deepcopy(parent1[idx]))
            offspring2.append(copy.deepcopy(parent2[idx]))

        # finishes the building of the offspring with the other parent
        # inserts the genes to the left of the second point
        for idx in range(p2 - 1, -1, -1):
            # the range goes from the second point to 0 in reverse order
            if chromosome.valid_insert(offspring1, parent2[idx]):
                offspring1.insert(0, copy.deepcopy(parent2[idx]))
            if chromosome.valid_insert(offspring2, parent1[idx]):
                offspring2.insert(0, copy.deepcopy(parent1[idx]))

        # appends the genes to the right of the second point
        for idx in range(p2, len(parent2)):
            if chromosome.valid_append(offspring1, parent2[idx]):
                offspring1.append(copy.deepcopy(parent2[idx]))
        for idx in range(p2, len(parent1)):
            if chromosome.valid_append(offspring2, parent1[idx]):
                offspring2.append(copy.deepcopy(parent1[idx]))

        return (offspring1, offspring2)
