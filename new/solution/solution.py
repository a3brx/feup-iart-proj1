from math import ceil
from random import choice, randrange, shuffle

from model.drone import Drone
from model.place import Client
from solution.operation import Operation


class DroneSimulation(Drone):
    def __init__(self, drone, position):
        super().__init__(drone.id)
        self.position = position
        self.tasks = []
    
    def distance_to(self, operand):
        return self.position.distance_to(operand.position)


class ClientSimulation(Client):
    def __init__(self, client):
        super().__init__(client.id, client.position.x, client.position.y, client.order)
        self.simulated_order = client.order.copy()


class Solution:
    def __init__(self, environment, items_clients, operations):
        self.environment = environment
        self.items_clients = items_clients.copy()
        self.operations = operations.copy()
        self.score = None

    def copy(self):
        def copy(operand):
            return operand.copy()
        copy_of_operations = list(map(copy, self.operations))
        return Solution(self.environment, self.items_clients, copy_of_operations)

    def get_score(self):
        if self.score == None:
            self.score = self.evaluate()
        return self.score

    @classmethod
    def initial(cls, environment):
        # Create lists of items by product
        items_by_product = {}
        for product in environment.products:
            items_by_product[product] = []
        for item in environment.items:
            items_by_product[item.product].append(item)

        # Assign clients to products
        items_clients = {}
        clients_sorted_by_order_size = sorted(environment.clients, key=len)
        for client in clients_sorted_by_order_size:
            for product in client.order:
                items_by_product[product].sort(
                    key=lambda x: x.origin.distance_to(client),
                    reverse=True
                )
                items_clients[items_by_product[product].pop()] = client

        # Create list of operations
        operations = []
        for item in items_clients:
            operations.append(
                Operation(item, items_clients[item], choice(environment.drones)))

        return Solution(environment, items_clients, operations)

    def evaluate(self):
        # Init drones
        drone_initial_position = self.environment.warehouses[0].position
        simulated_drones = [
            DroneSimulation(drone, drone_initial_position)
            for drone in self.environment.drones
        ]
        simulated_clients = list(map(ClientSimulation, self.environment.clients))
        for operation in self.operations:
            simulated_drones[operation.drone.id].tasks.append(operation)

        score = 0
        for drone in simulated_drones:
            turn = 0
            for task in drone.tasks:
                distance_to_warehouse = drone.distance_to(task.item.origin)
                distance_to_client = task.item.origin.distance_to(task.destination)
                turn += distance_to_warehouse + distance_to_client + 2
                if turn >= self.environment.number_of_turns:
                    break
                drone.position = task.destination.position
                client = simulated_clients[task.destination.id]
                client.simulated_order.remove(task.item.product)
                if not simulated_clients[client.id].simulated_order:
                    score += ceil((self.environment.number_of_turns - turn) / self.environment.number_of_turns * 100)
        return score
