from simulation.model.place import Place


class Warehouse(Place):

    def __init__(self, location, products_count):
        super().__init__(location)
        self.products_count = products_count

    def decrease_product(self, product_type):
        self.products_count[product_type] -= 1

    def increase_product(self, product_type):
        self.products_count[product_type] += 1
