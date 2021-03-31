"""Holds the chromosome class and helper functions.

Classes:

    Chromosome

Functions:

    valid_append(List[Path], Path)
    valid_insert(List[Path], Path)
"""


class Chromosome:
    """Represents a solution to the problem.

    Holds the solution and its fitness/evaluation.
    """

    def __init__(self, solution, fitness):
        """Instantiates a chromosome.

        ...
        Args:
            solution (List[Path]): The list of paths/steps of a solution
            fitness (integer): The fitness/evaluation of the solution
        """
        self.solution = solution
        self.fitness = fitness
