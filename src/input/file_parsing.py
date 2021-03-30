from simulation.simulation import Simulation
from simulation.environment import Environment
from simulation.model.order import Order
from simulation.model.warehouse import Warehouse
from simulation.model.product import Product


class FileParsing:

    @staticmethod
    def parse(path):
        with open(path) as f:
            contents = f.read().splitlines()

        if contents == None:
            raise Exception('Could not read file')

        environment = FileParsing.__parse_environment(contents)
        products = FileParsing.__parse_products(contents)
        warehouses = FileParsing.__parse_warehouses(contents)
        orders = FileParsing.__parse_orders(contents)

        return Simulation(environment, products, warehouses, orders)

    def __parse_environment(contents):
        environment_params = contents[0].split(' ')

        return Environment(int(environment_params[0]), int(environment_params[1]), int(environment_params[3]),
                           int(environment_params[2]), int(environment_params[4]))

    def __parse_products(contents):
        product_count = int(contents[1])
        product_params = list(map(int, contents[2].split(' ')))

        products = []

        for type, weight in zip(range(0, product_count), product_params):
            products.append(Product(type, weight))

        return products

    def __parse_warehouses(contents):
        warehouses_count = int(contents[3])
        warehouses_lines = contents[4:4 + warehouses_count*2]

        warehouses = []

        for i in range(0, warehouses_count):
            location_params = tuple(map(int, warehouses_lines[i*2].split(' ')))
            product_params = list(
                map(int, warehouses_lines[i*2 + 1].split(' ')))

            warehouses.append(Warehouse(location_params, product_params))

        return warehouses

    def __parse_orders(contents):
        warehouses_count = int(contents[3])
        orders_counts = int(contents[4 + warehouses_count*2])
        orders_lines = contents[5 + warehouses_count*2:]

        orders = []

        for i in range(0, orders_counts):
            location_params = tuple(map(int, orders_lines[i*2].split(' ')))
            product_types_params = list(
                map(int, orders_lines[i*2 + 2].split(' ')))

            orders.append(
                Order(location_params, product_types_params))

        return orders
