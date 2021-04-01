from model.place import Client, Warehouse
from model.item import Item, Product
from model.drone import Drone


class Data:
    def __init__(self, rows, columns, drones, turns, max_payload, warehouses, clients, products, items):
        super().__init__()
        self.number_of_rows = rows
        self.number_of_columns = columns
        self.number_of_turns = turns
        self.max_payload = max_payload

        # Tuples
        self.drones = tuple(map(Drone, range(drones)))
        self.warehouses = warehouses
        self.clients = clients
        self.products = products
        self.items = items

    item_count = 0

    @staticmethod
    def create_items(warehouse, items_quantity, products):
        items = []
        for product, quantity in enumerate(items_quantity):
            for _ in range(quantity):
                items.append(
                    Item(Data.item_count, products[product], warehouse))
                Data.item_count += 1
        return items

    @classmethod
    def from_input_file(cls, file):
        with open("data/" + file + ".in") as input_file:
            def read_int():
                return int(input_file.readline())

            def read_int_tuple():
                return tuple(map(int, input_file.readline().split()))

            def ignore_line():
                input_file.readline()

            # Problem
            problem_information = read_int_tuple()

            # Products
            ignore_line()  # number of products
            product_weights = read_int_tuple()
            products = []
            for product_id, weight in enumerate(product_weights):
                products.append(Product(product_id, weight))

            # Warehouses
            number_of_warehouses = read_int()
            warehouses = []
            items = []
            for i in range(number_of_warehouses):
                warehouse_coordinates = read_int_tuple()
                warehouse_products = read_int_tuple()
                new_warehouse = Warehouse(i, *warehouse_coordinates)
                items.extend(Data.create_items(
                    new_warehouse, warehouse_products, products))
                warehouses.append(new_warehouse)

            # Orders
            number_of_orders = read_int()
            clients = []
            for i in range(number_of_orders):
                client_coordinates = read_int_tuple()
                ignore_line()  # number of clients
                order = [products[x] for x in read_int_tuple()]
                clients.append(Client(i, *client_coordinates, order))

            return Data(*problem_information, warehouses, clients, products, items)
