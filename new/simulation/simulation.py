from math import ceil

from model.place import Client, Warehouse
from model.drone import Drone
from model.item import Item
from simulation.operation import Operation

DEBUG_PRINT = False


class WarehouseSimulation(Warehouse):
    def __init__(self, warehouse):
        super().__init__(warehouse.id, warehouse.position.x, warehouse.position.y)
        self.items = set()


class DroneSimulation(Drone):
    def __init__(self, drone_id, position):
        super().__init__(drone_id)
        self.ready = True
        self.position = position
        self.tasks = []

    def distance_to(self, operand):
        return self.position.distance_to(operand.position)


class ClientSimulation(Client):
    def __init__(self, client):
        super().__init__(client.id, client.position.x, client.position.y, client.initial_order)
        self.order = list(self.order)


class ItemSimulation(Item):
    def __init__(self, item):
        super().__init__(item.id, item.product, item.origin)
        self.location = item.origin
    
    def copy(self):
        return ItemSimulation(self.id, self.product, self.origin)


class Simulation:
    def __init__(self, environment, operations):
        self.environment = environment

        initial_drone_position = environment.warehouses[0].position
        self.drones = tuple([
            DroneSimulation(drone.id, initial_drone_position)
            for drone in environment.drones
        ])
        self.available_drones = set(self.drones)

        self.warehouses = tuple(
            map(WarehouseSimulation, environment.warehouses)
        )
        self.clients = tuple(
            map(ClientSimulation, environment.clients)
        )
        self.items = tuple(
            map(ItemSimulation, environment.items)
        )

        self.operations = [
            Operation(self.items[operation.item.id], operation.destination.copy(), self.drones[operation.drone.id]) for operation in operations
        ]

        self.events = {}
        for i in range(environment.number_of_turns):
            self.events[i] = []
        self.score = None

    def get_score(self):
        if self.score == None:
            self.score = self.evaluate()
        return self.score

    def add_event(self, turn, event_type, drone):
        if turn >= self.environment.number_of_turns:
            return
        self.events[turn].append((event_type, drone))

    def fly_drone(self, turn, drone, warehouse):
        if DEBUG_PRINT:
            print(turn, drone, "flying to location")
        end_of_task = turn + drone.distance_to(warehouse)
        drone.position = warehouse.position
        self.add_event(end_of_task, "fly", drone)

    def wait_item(self, turn, drone):
        if DEBUG_PRINT:
            print(turn, drone, "waiting for item")

    def make_task(self, turn, drone):
        if DEBUG_PRINT:
            print(turn, drone, "making operation")
        operation = drone.tasks[0]
        warehouse = self.warehouses[operation.item.location.id]
        warehouse.items.remove(operation.item)
        self.add_event(turn + 2 + drone.distance_to(operation.destination), "done", drone)

    def add_to_score(self, turn):
        self.score += ceil((self.environment.number_of_turns -
                           turn) / self.environment.number_of_turns * 100)

    def finalize_task(self, turn, drone):
        if DEBUG_PRINT:
            print(turn, drone, "done operation")
        operation = drone.tasks[0]
        warehouse = self.warehouses[operation.item.location.id]
        if isinstance(operation.destination, Client):
            operation.destination.order.remove(operation.item.product)
            if not operation.destination.order:
                self.add_to_score(turn)
        else:
            operation.item.location = operation.destination
        drone.tasks.pop(0)
        drone.position = operation.destination.position
        self.available_drones.add(drone)

    def process_events(self, turn):
        for event_type, drone in self.events[turn]:
            if event_type == "done":
                self.finalize_task(turn, drone)
            elif event_type == "fly":
                self.available_drones.add(drone)

    def evaluate(self):
        self.score = 0

        # Put the items in the warehouses
        for item in self.items:
            self.warehouses[item.origin.id].items.add(item)

        # Add operations to drones
        for operation in self.operations:
            self.drones[operation.drone.id].tasks.append(operation)

        # Simulate turns
        for turn in range(self.environment.number_of_turns):
            self.process_events(turn)
            new_unavailable_drones = set()
            for drone in self.available_drones:
                if not drone.tasks:
                    # Drone has finished all of its tasks
                    new_unavailable_drones.add(drone)
                    continue

                operation = drone.tasks[0]
                warehouse = self.warehouses[operation.item.location.id]
                if not drone.position == warehouse.position:
                    # Drone needs to fly to the specified location
                    self.fly_drone(turn, drone, warehouse)
                    new_unavailable_drones.add(drone)
                    continue

                if operation.item not in warehouse.items:
                    # Drone needs to wait for item
                    self.wait_item(turn, drone)
                    continue

                self.make_task(turn, drone)
                new_unavailable_drones.add(drone)

            self.available_drones = self.available_drones.difference(
                new_unavailable_drones)

        return self.score
