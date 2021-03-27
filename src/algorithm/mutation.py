from random import randrange, choice

from model.path import Path

def swap_operations(model):
    pass

def insert_operation(model):
    # Randomize path that will have a sucessor
    solution_length = len(model.solution)
    predecessor_path_index = randrange(solution_length)
    predecessor_path = model.solution[predecessor_path_index]

    # Create a new node with a random drone
    new_path = Path(predecessor_path.product, predecessor_path.destination)
    new_path.assign_drone(randrange(model.data.number_of_drones))

    # TODO: warehouse cannot be repeated
    new_warehouse = choice(model.warehouses)
    predecessor_path.destination = new_warehouse

    model.solution.insert(randrange(predecessor_path_index + 1, solution_length + 1), new_path)



def remove_operation(model):
    pass

def switch_operation_drone(model):
    pass