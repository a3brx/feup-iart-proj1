import copy
import itertools
from output.command import Command
from simulation.simulation import Simulation, euclidean_distance
from simulation.model.transportation import Delivery

def save_solution(solution, simulation, filename="solution.out"):
    commands = solution_commands(solution, simulation)
    commands = list(itertools.chain(*commands))

    file = open(filename, "w")
    file.write(str(len(commands)) + "\n")

    for command in commands:
        file.write(str(command) + "\n")

def solution_commands(solution, simulation):
    drone_count = simulation.environment.drones_count
    drone_jobs = [[] for _ in range(drone_count)]

    for transportation in solution:
        drone_jobs[transportation.drone].append(transportation)

    # builds deliveries for the drones
    # ie joining of transportation
    deliveries = []
    for job in drone_jobs:
        deliveries.append(Delivery.build_deliveries(
            job, simulation.environment.drone_max_payload))

    # copies the orders to not complete the original ones
    delivered_orders = copy.deepcopy(simulation.orders)

    drone_commands = [[] for _ in range(drone_count)]

    current_drone = 0

    for drone in deliveries:
        # the starting location of the drone
        location = simulation.warehouses[0].location
        total_turns = 0

        commands = []

        # completes all the deliveries of the drone
        for delivery in drone:
            # realizes a deliver, updating the drone location and number of turns taken
            turns, location, new_commands = moves(delivery, location)
            total_turns += turns

            # if the total number of turns is exceeded, doesn't count anymore
            if total_turns >= simulation.environment.turns:
                break

            commands.extend(new_commands)

            # updates the order of that delivery if it applies
            Simulation.update_order(
                delivered_orders, delivery, total_turns)

        drone_commands[current_drone] = commands
        current_drone += 1

    return drone_commands

def moves(delivery, drone_position):
        """Calculates the number of turns it takes to deliver a delivery and its commands.

        ...
        Parameters:
            delivery (Delivery): The delivery to deliver
            drone_position ((integer, integer)): The initial drone position

        Returns:
            (integer, (integer, integer), List(Command)): The number of turns it takes, the final position of the drone, and the list of commands
        """
        commands = []

        products = {}

        for product in delivery.products:
            if product.type not in products:
                products[product.type] = 1
            else:
                products[product.type] += 1
            
        for product_type, product_count in products.items():
            commands.append(Command(delivery.drone, command="L", warehouse_id=delivery.source.id, product_type=product_type, number_of_items=product_count))

        turns = 0

        # distance to source
        distance_to_source = euclidean_distance(drone_position, delivery.source.location)
        turns += distance_to_source

        # pickup the products
        # TODO verify if the products are there, tenso
        turns += delivery.product_types

        # take the products to destination
        turns += euclidean_distance(delivery.source.location,
                                    delivery.destination.location)

        # drops the prodcts
        turns += delivery.product_types

        for product_type, product_count in products.items():
            commands.append(Command(delivery.drone, command="D", customer_id=delivery.source.id, product_type=product_type, number_of_items=product_count))

        return (turns, delivery.destination.location, commands)