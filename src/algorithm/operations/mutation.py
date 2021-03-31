from simulation.model.order import Order
from simulation.model.warehouse import Warehouse
from random import randrange


def exchange_positions(solution):
    """Exchanges two positions in a solution.

    ...
    Args:
        solution (List[Transportation]): The list of transportations of the solution
    """

    valid_move = False

    while not valid_move:
        mutated_solution = solution.copy()

        position1, position2 = __random_positions(len(solution))
        product1, product2 = mutated_solution[position1].product, mutated_solution[position2].product

        mutated_solution[position1], mutated_solution[position2] = mutated_solution[position2], mutated_solution[position1]

        valid_move = valid_transportation_exchange(
            mutated_solution, product1) and valid_transportation_exchange(mutated_solution, product2)

    return mutated_solution


def valid_transportation_exchange(solution, product):
    """Checks whether a transportation exchange is valid or not.

    A transportation exchange is valid if no transportation of a product from
    a warehouse to another warehouse is placed after a transportation of the
    same product from a warehouse to the client.
    """

    found_move = False

    for transportation in solution:
        if transportation.product != product:
            continue

        # If the move is already found and the transportation is to a warehouse then the
        # transportation is not valid
        if found_move and isinstance(transportation.destination, Warehouse):
            return False
        elif not found_move and isinstance(transportation.destination, Order):
            found_move = True

    return True


def __random_positions(max_position):
    """Generates two random different list positions given a max position. The max position is exclusive.

    ...
    Args:
        max_position (integer): The maximum position
    """

    lhs = randrange(max_position)
    rhs = randrange(max_position)

    while rhs == lhs:
        rhs = randrange(max_position)

    return (lhs, rhs)
