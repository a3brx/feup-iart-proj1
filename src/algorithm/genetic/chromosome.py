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


def valid_append(solution, path):
    """Verifies if the appending of a path to a solution (or the appending of a gene to a chromosome) is valid.

    For a chromosome/solution to be valid, the following points have to be veirified:
        - A gene that transports a product to a warehouse cannot appear after a gene that transports the same
            product to its final destination by the same drone;
        - A chromosome cannot have genes that transport a product to a warehouse it has been before;
        - A chromosome must have one and only one gene that transports a product to its final destination;
        - A chromsome cannot have repeated genes, this is, genes with the same product and destination.

    ...
    Args:
        solution (List[Path]): A solution with a list of paths
        path (Path): The path to try to append

    Returns:
        boolean: True if the appending is valid, False otherwise
    """
    # TODO
    return True


def valid_insert(solution, path):
    """Verifies if the insertion of a path at the beginning of a solution is valid.

    For a chromosome/solution to be valid, the following points have to be veirified:
        - A gene that transports a product to a warehouse cannot appear after a gene that transports the same
            product to its final destination by the same drone;
        - A chromosome cannot have genes that transport a product to a warehouse it has been before;
        - A chromosome must have one and only one gene that transports a product to its final destination;
        - A chromsome cannot have repeated genes, this is, genes with the same product and destination.

    ...
    Args:
        solution (List[Path]): A solution with a list of paths
        path (Path): The path to try to append

    Returns:
        boolean: True if the insertion is valid, False otherwise
    """
    # TODO
    return True
