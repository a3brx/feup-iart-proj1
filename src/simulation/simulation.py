import math
from random import randrange
from simulation.model.warehouse import Warehouse
from simulation.model.transportation import Transportation


def euclidean_distance(location_lhs, location_rhs):
    lhs_x, lhs_y = location_lhs
    rhs_x, rhs_y = location_rhs

    return int(math.ceil(math.sqrt(math.pow(rhs_x - lhs_x, 2) + math.pow(rhs_y - lhs_y, 2))))


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

    def deliver(self, delivery, drone_position):
        """Calculates the number of turns it takes to deliver a delivery.

        ...
        Args:
            delivery (Delivery): The delivery to deliver
            drone_position ((integer, integer)): The initial drone position

        Returns:
            (integer, (integer, integer)): The number of turns it takes, and the final position of the drone
        """
        turns = 0

        # distance to source
        turns += euclidean_distance(drone_position, delivery.source.location)

        # pickup the products
        # TODO verify if the products are there, tenso
        turns += delivery.product_types

        # take the products to destination
        turns += euclidean_distance(delivery.source.location,
                                    delivery.destination.location)

        # drops the prodcts
        turns += delivery.product_types

        return (turns, delivery.destination.location)

    def update_order(orders, delivery):
        """Updates the remaining products in an order, according to a delivery.

        ...
        Args:
            orders (list[Order]): The list of orders to update
            delivery (Delivery): The delivery to take into account

        Returns:
            Order: The order that was completed, None if none was
        """
        for order in orders:
            if order.location == delivery.destination.location:
                for product in delivery.products:
                    order.remove(product.type)
                    return order

        return None
