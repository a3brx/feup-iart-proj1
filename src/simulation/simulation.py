import math
from random import randrange
from simulation.model.warehouse import Warehouse
from simulation.model.transportation import Transportation


def euclidean_distance(location_lhs, location_rhs):
    lhs_x, lhs_y = location_lhs
    rhs_x, rhs_y = location_rhs

    return math.sqrt(math.pow(rhs_x - lhs_x, 2) + math.pow(rhs_y - lhs_y, 2))


class Simulation:

    def __init__(self, environment, products, warehouses, orders):
        self.environment = environment
        self.products = products
        self.warehouses = warehouses
        self.orders = orders

    def order_weight(self, order_id):
        return sum([
            self.products[product_type] for product_type in self.orders[order_id].product_types])

    def closest_warehouse(self, location, product_type):
        warehouses = sorted(self.warehouses, key=lambda warehouse: euclidean_distance(
            location, warehouse.location))

        warehouse = next((warehouse for warehouse in warehouses if warehouse.product(
            product_type) is not None), None)

        if warehouse is not None:
            return (warehouse, warehouse.product(product_type))

        return None

    def random_drone(self):
        return randrange(0, self.environment.drones_count)

    def assign_transportation(self, warehouse, drone, product, destination):
        warehouse.decrease_product(product.type)

        if isinstance(destination, Warehouse):
            destination.increase_product(product)

        return Transportation(product, drone, warehouse, destination)
