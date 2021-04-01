"""Holds crossover classes used in genetic algorithms.

Classes:

    Crossover
    OnePointCrossover
    OrderCrossover
"""

from abc import ABC, abstractmethod
import algorithm.operation.restriction as restriction
import copy
import random


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
        [smaller, larger] = sorted((parent1, parent2), key=lambda parent: len(parent))
        min_size = len(smaller)
        cut_point = random.randint(1, min_size - 1)

        # starts the offsprings with the first part of the parents
        offspring1 = []
        offspring2 = []

        offspring1_hashes_source = set()
        offspring2_hashes_source = set()

        offspring1_hashes_destination = set()
        offspring2_hashes_destination = set()

        for idx in range(cut_point):
            gene1 = copy.copy(smaller[idx])
            gene2 = copy.copy(larger[idx])

            offspring1.append(gene1)
            offspring2.append(gene2)

            offspring1_hashes_source.add(gene1.hash_source())
            offspring2_hashes_source.add(gene2.hash_source())

            offspring1_hashes_destination.add(gene1.hash_destination())
            offspring2_hashes_destination.add(gene2.hash_destination())

        # finishes the building of the offspring with the other parent
        for idx in range(0, min_size):
            if restriction.valid_insert(offspring1_hashes_source, offspring1_hashes_destination, larger[idx]):
                offspring1.append(copy.copy(larger[idx]))
            if restriction.valid_insert(offspring2_hashes_source, offspring2_hashes_destination, smaller[idx]):
                offspring2.append(copy.copy(smaller[idx]))

        for idx in range(min_size, len(larger)):
            if restriction.valid_insert(offspring1_hashes_source, offspring1_hashes_destination, larger[idx]):
                offspring1.append(copy.copy(larger[idx]))

        return (copy.deepcopy(offspring1), copy.deepcopy(offspring2))


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
        [smaller, larger] = sorted((parent1, parent2), key=lambda parent: len(parent))
        min_size = len(smaller)
        points = random.sample(range(1, min_size - 1), 2)
        [p1, p2] = sorted(points)

        # starts the offsprings with the sequence between the points in the parents
        offspring1 = []
        offspring2 = []

        offspring1_hashes_source = set()
        offspring2_hashes_source = set()

        offspring1_hashes_destination = set()
        offspring2_hashes_destination = set()

        for idx in range(p1, p2):
            gene1 = copy.copy(smaller[idx])
            gene2 = copy.copy(larger[idx])

            offspring1.append(gene1)
            offspring2.append(gene2)

            offspring1_hashes_source.add(gene1.hash_source())
            offspring2_hashes_source.add(gene2.hash_source())

            offspring1_hashes_destination.add(gene1.hash_destination())
            offspring2_hashes_destination.add(gene2.hash_destination())

        # finishes the building of the offspring with the other parent
        # inserts the genes to the left of the second point
        for idx in range(p2 - 1, -1, -1):
            # the range goes from the second point to 0 in reverse order
            if restriction.valid_insert(offspring1_hashes_source, offspring1_hashes_destination, larger[idx]):
                offspring1.insert(0, copy.copy(larger[idx]))
            if restriction.valid_insert(offspring2_hashes_source, offspring2_hashes_destination, parent1[idx]):
                offspring2.insert(0, copy.copy(smaller[idx]))

        # appends the genes to the right of the second point
        for idx in range(p2, min_size):
            if restriction.valid_insert(offspring1_hashes_source, offspring1_hashes_destination, larger[idx]):
                offspring1.append(copy.copy(larger[idx]))
            if restriction.valid_insert(offspring2_hashes_source, offspring2_hashes_destination, smaller[idx]):
                offspring2.append(copy.copy(smaller[idx]))

        for idx in range(min_size, len(larger)):
            if restriction.valid_insert(offspring1_hashes_source, offspring1_hashes_destination, larger[idx]):
                offspring1.append(copy.copy(larger[idx]))

        return (offspring1, offspring2)
