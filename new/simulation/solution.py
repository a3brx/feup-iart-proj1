from random import choice, randrange, shuffle

from simulation.operation import Operation
from simulation.simulation import Simulation


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
            self.score = Simulation(self.environment, self.operations).evaluate()
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
