"""Holds the genetic approach for the solution of the problem.

Classes:

    GeneticAlgorithm
"""

from timeit import default_timer as timer
import copy

from algorithm.genetic.selection import RoulleteSelection
from algorithm.genetic.crossover import OrderCrossover
from algorithm.genetic.chromosome import Chromosome
from algorithm.algorithm import Algorithm


class GeneticAlgorithm(Algorithm):
    """Problem solver resorting to genetic algorithm.

    In genetic algorithms, solutions (called chromosomes) suffer mutations and are crossover between themselves,
    so that new solutions are generated.

    Holds its environment, time and iterations ceil, parent selection method, population size and if it is generational
    or iterative.
    """

    def __init__(self, environment, time=None, iterations=None, selection_method=None, crossover=None, population_size=30, generational=True):
        """Instantiates a genetic algorithm.

        ...
        Args:
            environment (Environment): The environment of the problem
            time (real): The max time in seconds the algorithm should take
            iterations (integer): The max number of iterations the algorithm should take
            selection_method (SelectionMetohd): The parent selection method, this is, the method used to select parents
                                                for crossover. Roullete selection if none is passed
            crossover (Crossover): The crossover method to reproduce between two chromosomes. The default is the order
                                   crossover
            population_size (integer): The size of the population. The default is 30
            generational (boolean): Identifies if the offsprings should replace the parents per iteractions. If true,
                                    the number of offsprings generated is the same as the size of the population and
                                    this offsprings replace the old population. If false, when one offspring i
                                    generated, the weakest chromosome in the population is removed to give space to the
                                    new offspring. The default is true
        """
        super().__init__(environment, time, iterations)

        self.selection_method = \
            RoulleteSelection() if selection_method is None else selection_method
        self.crossover = OrderCrossover() if crossover is None else crossover

        self.population_size = population_size
        self.generational = generational

    def run(self):
        """Runs the genetic algorithm.

        ...
        Returns:
            Chromosome: The best chromosome solution
        """
        self.starting_time = timer()

        # builds the initial solution
        population = self.random_population()

        while not self.stop_condition():
            if (self.generational):
                # creates the required number of offsprings and replaces the old population
                population = self.__new_generation(population)

            else:
                # creates one offspring, adds it to the population, and removes the worst offspring in there
                (parent1, parent2) = self.selection_method.run(population)
                (offspring1, offspring2) = self.crossover.run(
                    parent1.solution, parent2.solution)

                offspring1 = self.mutate(offspring1)
                offspring2 = self.mutate(offspring2)

                population.append(Chromosome(
                    offspring1, self.evaluate(offspring1)))
                population.append(Chromosome(
                    offspring2, self.evaluate(offspring2)))

                population.remove(
                    min(population, key=lambda chromosome: chromosome.fitness))
                population.remove(
                    min(population, key=lambda chromosome: chromosome.fitness))

        # gets the best solution of the current population and returns it
        # TODO maybe store overall best solution instead of this one
        solution = self.best_solution(population)
        return copy.deepcopy(solution)

    def mutate(self, chromosome):
        # TODO
        return chromosome

    def stop_condition(self):
        # TODO complete with a number of iterations without improving or something
        return super().stop()

    def random_population(self):
        """Builds a random population with chromosomes with random solutions.

        ...
        Returns:
            list[Chromosome]: A list of chromosomes with random solutions.
        """
        res = []
        for _ in range(self.population_size):
            solution = self.random_solution()
            chromosome = Chromosome(solution, self.evaluate(solution))

            res.append(chromosome)

        return res

    def best_solution(self, population):
        """Gets the best chromosome in a population

        ...
        Args:
            population (list[Chromosome]): The list of chromsomes that constitute the population

        Returns:
            Chromsome: The best chromosome
        """
        return max(population, key=lambda chromosome: chromosome.fitness)

    def __new_generation(self, population):
        """Gets a new generation using crossover between chrosomes in a given population.

        ...
        Args:
            population (list[Chrosome]): The current population

        Returns:
            list[Chrosome]: A new chrosome generation
        """
        new_population = []
        for _ in range(self.population_size // 2):
            (parent1, parent2) = self.selection_method.run(population)
            (offspring1, offspring2) = self.crossover.run(parent1, parent2)
            offspring1 = self.mutate(offspring1)
            offspring2 = self.mutate(offspring2)
            new_population.append(offspring1, offspring2)

        return new_population
