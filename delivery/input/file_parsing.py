from delivery.simulation.simulation import Simulation
from delivery.simulation.environment import Environment
from delivery.simulation.model.order import Order
from delivery.simulation.model.warehouse import Warehouse
from delivery.simulation.model.product import Product


def parse(path):
    with open(path) as f:
        contents = f.read().splitlines()

    if contents == None:
        raise Exception('Could not read file')

    environment = __parse_environment(contents)
    product_weights = __parse_products(contents)
    warehouses = __parse_warehouses(contents, product_weights)
    orders = __parse_orders(contents)

    return Simulation(environment, product_weights, warehouses, orders)


def __parse_environment(contents):
    environment_params = contents[0].split(' ')

    return Environment(int(environment_params[0]), int(environment_params[1]), int(environment_params[3]),
                       int(environment_params[2]), int(environment_params[4]))


def __parse_products(contents):
    Product.id = 0
    product_params = list(map(int, contents[2].split(' ')))

    products = []

    for weight in product_params:
        products.append(weight)

    return products


def __parse_warehouses(contents, product_weights):
    Warehouse.id = 0
    warehouses_count = int(contents[3])
    warehouses_lines = contents[4:4 + warehouses_count*2]

    warehouses = []

    for i in range(0, warehouses_count):
        location_params = tuple(map(int, warehouses_lines[i*2].split(' ')))
        product_params = list(
            map(int, warehouses_lines[i*2 + 1].split(' ')))

        products = []
        for product_type, product_count in zip(range(0, len(product_params)), product_params):
            for i in range(0, product_count):
                products.append(
                    Product(product_type, product_weights[product_type]))

        warehouses.append(Warehouse(location_params, products))

    return warehouses


def __parse_orders(contents):
    Order.id = 0
    warehouses_count = int(contents[3])
    orders_counts = int(contents[4 + warehouses_count*2])
    orders_lines = contents[5 + warehouses_count*2:]

    orders = []

    for i in range(0, orders_counts):
        location_params = tuple(map(int, orders_lines[i*3].split(' ')))
        product_types_params = list(
            map(int, orders_lines[i*3 + 2].split(' ')))

        orders.append(
            Order(location_params, product_types_params))

    return orders
