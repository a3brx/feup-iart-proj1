import copy
import random


def exchange_positions(solution, _):
    """Exchanges two positions in a solution.

    ...
    Parameters:
        solution (List[Transportation]): The list of transportations of the solution
    """
    mutated_solution = solution.copy()
    position1, position2 = __random_positions(len(solution))

    mutated_solution[position1], mutated_solution[position2] = mutated_solution[position2], mutated_solution[position1]

    return mutated_solution


def modify_drone(solution, simulation):
    """Modifies the drone of a random operation.

    ...
    Parameters:
        solution(List[Transportation]): The list of the transportations of the solution
        simulation(Simulation): The simulation

    Returns:
        List[Transportation]: The modified solution
    """
    solution = solution.copy()

    random_operation = random.randrange(0, len(solution))
    new_drone = simulation.random_drone()

    # Continues to generate a random drone while the drone generated
    # is the same as the drone previously assigned
    while solution[random_operation].drone == new_drone:
        new_drone = simulation.random_drone()

    # Copies the transportation in order to change its drone
    # only in the mutated solution
    transportation = copy.deepcopy(solution[random_operation])
    transportation.drone = new_drone

    # Assigns the transportation with the new drone to its position
    solution[random_operation] = transportation

    return solution


def __random_positions(max_position):
    """Generates two random different list positions given a max position.
    The max position is exclusive.

    ...
    Args:
        max_position(integer): The maximum position
    """
    [lhs, rhs] = random.sample(range(0, max_position - 1), 2)

    return (lhs, rhs)
