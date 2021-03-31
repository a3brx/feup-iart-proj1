from algorithm.operation.restriction import valid_transportation_exchange
from copy import deepcopy
import random


def exchange_positions(solution):
    """Exchanges two positions in a solution.

    ...
    Args:
        solution (List[Transportation]): The list of transportation of the solution
    """

    valid_move = False

    while not valid_move:
        mutated_solution = deepcopy(solution)

        position1, position2 = __random_positions(len(solution))
        product1, product2 = mutated_solution[position1].product, mutated_solution[position2].product

        mutated_solution[position1], mutated_solution[position2] = mutated_solution[position2], mutated_solution[position1]

        valid_move = valid_transportation_exchange(
            mutated_solution, product1) and valid_transportation_exchange(mutated_solution, product2)

    return mutated_solution


def __random_positions(max_position):
    """Generates two random different list positions given a max position. The max position is exclusive.

    ...
    Args:
        max_position (integer): The maximum position
    """

    [lhs, rhs] = random.sample(range(0, max_position - 1), 2)

    return (lhs, rhs)
