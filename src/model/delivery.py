from random import randrange, shuffle
from math import ceil

from model.path import Path
from model.place import Client, Warehouse
from model.product import Product


class Data:
    def __init__(self, rows, columns, drones, turns, payload, weights):
        self.number_of_rows = int(rows)
        self.number_of_columns = int(columns)
        self.number_of_drones = int(drones)
        self.number_of_turns = int(turns)
        self.max_payload = int(payload)
        self.product_weights = tuple(map(int, weights))

    def evaluate_solution(self, solution):
        turns = self.number_of_drones * [self.number_of_turns]
        score = 0
        factor = 1 / self.number_of_turns * 100
        for path in solution:
            # TODO: Take into account the time a drone needs to go to the next warehouse before delivering it
            turns[path.drone] -= path.duration()
            if turns[path.drone] < 0:
                continue
            score += ceil(turns[path.drone] * factor)
        return score


class Delivery:
    def __init__(self, data, warehouses, clients, solution=None):
        self.warehouses = warehouses
        self.clients = clients
        self.products = [
            product for warehouse in warehouses for product in warehouse.products
        ]
        self.data = data
        self.solution = self.initialize_solution() if solution == None else solution

    def copy(self):
        copy_of_warehouses = [
            warehouse.copy()
            for warehouse in self.warehouses
        ]
        copy_of_solution = [
            path.copy()
            for path in self.solution
        ]
        return Delivery(self.data, copy_of_warehouses, self.clients.copy(), copy_of_solution)

    def initialize_solution(self):
        # Assign products
        products_not_assigned = {}
        for product in self.products:
            if not product.product_type in products_not_assigned.keys():
                products_not_assigned[product.product_type] = []
            products_not_assigned[product.product_type].append(product)

        orders_sorted_by_size = sorted(self.clients, key=len)
        for order in orders_sorted_by_size:
            for product_type in order.wanted_products:
                products_not_assigned_of_type = products_not_assigned[product_type]
                products_not_assigned_of_type.sort(
                    key=order.distance_to_product, reverse=True)
                products_not_assigned_of_type.pop().assign_order(order)

        solution = list(
            map(Path, filter(lambda x: x.has_order(), self.products))
        )
        shuffle(solution)

        # Assign drones
        for path in solution:
            path.assign_drone(randrange(self.data.number_of_drones))

        return sorted(solution, key=lambda x: x.drone)

    def to_output_file(self, file):
        with open("data/" + file + ".out", "w+") as output_file:
            output_file.write(str(2 * len(self.solution)) + "\n")
            for path in self.solution:
                output_file.write(path.get_output_string())

    def evaluate_solution(self):
        return self.data.evaluate_solution(self.solution)

    @classmethod
    def from_input_file(cls, file):
        with open("data/" + file + ".in") as input_file:
            # Problem
            problem_information = input_file.readline().split()
            number_of_products = input_file.readline()
            product_weights = input_file.readline().split()

            # Warehouses
            number_of_warehouses = int(input_file.readline())
            warehouses = []
            for i in range(number_of_warehouses):
                warehouse_coordinates = input_file.readline().split()
                warehouse_items = input_file.readline().split()
                new_warehouse = Warehouse(
                    i, warehouse_coordinates, warehouse_items)
                warehouses.append(new_warehouse)

            # Orders
            number_of_orders = int(input_file.readline())
            clients = []
            for i in range(number_of_orders):
                order_coordinates = input_file.readline().split()
                order_number_of_items = input_file.readline()
                order_products = input_file.readline().split()
                new_client = Client(i, order_coordinates, order_products)
                clients.append(new_client)
            data = Data(*problem_information, product_weights)
            return Delivery(data, warehouses, clients)
