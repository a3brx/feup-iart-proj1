from random import choice, randrange

from delivery.solution.operation import Operation

def swap_operations(solution):
    solution_length = len(solution.operations)
    first_operation_index = randrange(solution_length)
    second_operation_index = choice(list(filter(lambda x: x != first_operation_index, range(solution_length))))

    solution.operations[first_operation_index], solution.operations[second_operation_index] = solution.operations[second_operation_index], solution.operations[first_operation_index]
    return True

def switch_operation_drone(solution):
    operation_to_switch = randrange(len(solution.operations))

    old_drone = solution.operations[operation_to_switch].drone
    new_drone = choice(list(filter(lambda x: x != old_drone, solution.environment.drones)))

    solution.operations[operation_to_switch].drone = new_drone
    return True

def swap_order_items(solution):
    solution_length = len(solution.operations)

    first_operation_index = randrange(solution_length)
    first_operation = solution.operations[first_operation_index]

    possible_operations = list(filter(
        lambda x: x != first_operation_index and first_operation.item.product == solution.operations[x].item.product,
        range(solution_length)
    ))

    if not possible_operations:
        return False

    second_operation_index = choice(possible_operations)
    second_operation = solution.operations[second_operation_index]

    first_operation.item, second_operation.item = second_operation.item, first_operation.item
    return True