from random import choice, randrange

from simulation.operation import Operation

def swap_operations(solution):
    failed_first_operations = set()

    solution_length = len(solution.operations)
    first_operation_index = randrange(solution_length)
    first_operation = solution.operations[first_operation_index]

    # Filter operations that can be selected
    possible_operations = list(enumerate(range(solution_length)))
    enumerated_solution = list(enumerate(solution.operations))
    items_final_before = [
        x for x in
        filter(
            lambda x: x[1].is_final(),
            enumerated_solution[:first_operation_index + 1]
        )
    ]
    items_not_final_after = [
        x for x in
        filter(
            lambda x: not x[1].is_final(),
            enumerated_solution[first_operation_index + 1:]
        )
    ]

    def possible(x):
        i, operation = x
        if i == first_operation_index:
            return False
        operation = solution.operations[operation]
        if operation.is_final():
            return operation.item not in items_not_final_after
        else:
            return operation.item not in items_final_before
    possible_operations = tuple(filter(possible, possible_operations))
    if not possible_operations:
        return False

    # Choose an operation and make the swap
    second_operation_index = choice(possible_operations)[0]
    solution.operations[first_operation_index], solution.operations[second_operation_index] = solution.operations[second_operation_index], solution.operations[first_operation_index]
    return True

def insert_operation(solution):
    # Randomize path that will have a sucessor
    solution_length = len(solution.operations)
    predecessor_operation_index = randrange(solution_length)
    predecessor_operation = solution.operations[predecessor_operation_index]

    # Create a new node with a random drone
    new_operation = Operation(predecessor_operation.item, predecessor_operation.destination, choice(solution.environment.drones))

    # Warehouse must be not in any other operation of that item
    all_warehouses = set(solution.environment.warehouses)
    used_warehouses = set([
        x.destination for x in
        filter(lambda x: x.item == new_operation.item, solution.operations)
    ])
    not_used_warehouses = list(all_warehouses.difference(used_warehouses))
    if not not_used_warehouses:
        return False
    new_warehouse = choice(not_used_warehouses)

    # Change the destination of the predecessor
    predecessor_operation.destination = new_warehouse

    if new_operation.is_final():
        last_index = solution_length + 1
    else:
        last_index = next((i for i in range(len(solution.operations) - 1, -1) if solution.operations[i].is_final() and solution.operations[i].product == new_operation.product), None)

    # Insert the new operation that has the same destination as the predecessor
    solution.operations.insert(
        randrange(predecessor_operation_index + 1, last_index), new_operation
    )

    return True

def remove_operation(solution):
    # Randomize operation that will be removed, it can only be a path to a warehouse
    solution_length = len(solution.operations)
    valid_operations_to_remove = tuple(
        filter(lambda x: not solution.operations[x].is_final(), range(solution_length)))
    if not valid_operations_to_remove:
        return False
    index_to_remove = choice(valid_operations_to_remove)

    # Remove the element
    solution.operations.pop(index_to_remove)
    return True

def switch_operation_drone(solution):
    solution_length = len(solution.operations)
    operation_to_switch = randrange(solution_length)
    old_drone = solution.operations[operation_to_switch].drone
    new_drone = old_drone
    while new_drone == old_drone:
        new_drone = choice(solution.environment.drones)
    solution.operations[operation_to_switch].drone = new_drone
    return True
