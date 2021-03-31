from random import randrange, choice

from model.path import Path
from model.place import Client


def swap_operations(model):
    solution_length = len(model.solution)
    first_operation_index = randrange(solution_length)
    first_operation = model.solution[first_operation_index]

    # Filter operations that can be selected
    possible_operations = list(enumerate(range(solution_length)))
    enumerated_solution = list(enumerate(model.solution))
    products_final_before = [
        x for x in
        filter(
            lambda x: x[1].is_final(),
            enumerated_solution[:first_operation_index + 1]
        )
    ]
    products_not_final_after = [
        x for x in
        filter(
            lambda x: not x[1].is_final(),
            enumerated_solution[first_operation_index:]
        )
    ]

    def possible(x):
        i, operation = x
        operation = model.solution[operation]
        if operation.is_final():
            return operation.product not in products_not_final_after
        else:
            return operation.product not in products_final_before
    possible_operations = tuple(filter(possible, possible_operations))

    # Choose an operation and make the swap
    second_operation_index = choice(possible_operations)[0]
    model.solution[first_operation_index], model.solution[second_operation_index] = model.solution[second_operation_index], model.solution[first_operation_index]
    return True


def insert_operation(model):
    # Randomize path that will have a sucessor
    solution_length = len(model.solution)
    predecessor_path_index = randrange(solution_length)
    predecessor_path = model.solution[predecessor_path_index]

    # Create a new node with a random drone
    new_path = Path(predecessor_path.product, predecessor_path.destination)
    new_path.assign_drone(randrange(model.data.number_of_drones))

    # Warehouse must be not in any other path of that product
    all_warehouses = set(model.warehouses)
    used_warehouses = set([x.destination for x in filter(
        lambda x: x.product == new_path.product, model.solution)])
    not_used_warehouses = list(all_warehouses.difference(used_warehouses))
    if not not_used_warehouses:
        return False
    new_warehouse = choice(not_used_warehouses)

    # Change the distination of the predecessor
    predecessor_path.destination = new_warehouse

    # Insert the new operation that has the same destination as the predecessor
    model.solution.insert(
        randrange(predecessor_path_index + 1, solution_length + 1), new_path)
    return True


def remove_operation(model):
    # Randomize operation that will be removed, it can only be a path to a warehouse
    solution_length = len(model.solution)
    valid_operations_to_remove = tuple(
        filter(lambda x: not model.solution[x].is_final(), range(solution_length)))
    if not valid_operations_to_remove:
        return False
    index_to_remove = choice(valid_operations_to_remove)

    # Remove the element
    model.solution.pop(index_to_remove)
    return True


def switch_operation_drone(model):
    solution_length = len(model.solution)
    operation_to_switch = randrange(solution_length)
    old_drone = model.solution[operation_to_switch].drone
    new_drone = old_drone
    while new_drone == old_drone:
        new_drone = randrange(model.data.number_of_drones)
    model.solution[operation_to_switch].drone = new_drone
    return True
