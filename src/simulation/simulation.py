class Simulation:

    def __init__(self, environment, products, warehouses, orders):
        self.environment = environment
        self.products = products
        self.warehouses = warehouses
        self.orders = orders

    def order_weight(self, order_id):
        return sum([
            self.products[product_type].weight for product_type in self.orders[order_id].product_types])
