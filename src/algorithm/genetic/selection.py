"""Defines selection methods for genetic algorithms.

Classes:

    SelectionMethod
    RoulleteSelection
    TournamentSelection
"""

from abc import ABC, abstractmethod
import random


class SelectionMethod(ABC):
    """Defines the selection methods. 

    Defines the possible selection methods, as well as how they run, for genetic algorithms.
    A selection method is responsible for selecting two parent chromosomes to crossover.
    """

    @abstractmethod
    def run(self, population):
        """Selects two parent chromosomes from a population to crossover.

        ...
        Args:
            population (List[Chromosome]): The current chromosome population

        Returns:
            ((Chromosome, Chromosome)): The selected parent chromosomes
        """
        pass


class RoulleteSelection(SelectionMethod):
    """Selects two chromosomes randomly according to their fitness.

    Also know as "fitness proportionate selection", associates the chromosomes' fitness level with a probability of
    selection. This probability is the same as the fitness of the chromosome in comparison with the fitness of the
    whole population. This is, if "f_i" is the fitness of the chromosome "i", its calculated as prob(a) = f_0/sum(f_i).
    """

    def run(self, population):
        """Runs the roullete selection.

        ...
        Args:
            population (List[Chromosome]): The current chromosome population

        Returns:
            (Chromosome, Chromosome): The selected parent chromosomes
        """

        # random.sample is used since the chromosome fitness is required to be an integer
        result_list = random.sample(
            population=population,
            counts=[chromosome.fitness for chromosome in population],
            k=2
        )
        return tuple(result_list)


class TournamentSelection(SelectionMethod):
    """Selects two chromosomes creating two random groups, selecting the best chromosome on both of them

    Tournament selection involves running two tournaments among a few chromosomes chosen at random from the population.
    The winner of each tournament (the one with the best fitness) is selected for crossover.
    """

    def __init__(self, competitor_amount):
        """Instantiates the tournament selection.

        ...
        Args:
            competitor_amount (integer): The number of competitors per tournament. This value is capped at half the
                                        size of the population and set to be at least 1. If the value is set to 1,
                                        the selections are just random
        """
        self.competitor_amount = competitor_amount

    @property
    def competitor_amount(self):
        """Gets the number of competitors per tournament.

        ...
        Returns:
            integer: The competitor amount
        """
        return self.__competitor_amount

    @competitor_amount.setter
    def competitor_amount(self, competitor_amount):
        """Sets the competitor amount

        Sets the value to at least 1.

        ...
        Args:
            competitor_amount (integer): the number of competitors per tournament
        """
        self.__competitor_amount = 1 if competitor_amount < 1 else competitor_amount

    def run(self, population):
        """Runs the tournament selection.

        The competitor amount value is capped at half of the size of the population.

        ...
        Args:
            population (List[Chromosome]): The current chromosome population

        Returns:
            (Chromosome, Chromosome): The selected parent chromosomes
        """
        max_competitor_amount = len(population) // 2
        competitor_amount = max_competitor_amount if self.competitor_amount > max_competitor_amount else self.competitor_amount

        # picks the chromosomes for the tournaments
        # random.sample is used since the chromosome fitness is required to be an integer
        result_list = random.sample(
            population,
            k=competitor_amount*2
        )

        # creates the tournaments
        random.shuffle(result_list)
        tournament1 = result_list[:competitor_amount]
        tournament2 = result_list[competitor_amount:]

        # selects the winner chromosomes
        c1 = max(tournament1, key=lambda chromosome: chromosome.fitness)
        c2 = max(tournament2, key=lambda chromosome: chromosome.fitness)
        return (c1, c2)
