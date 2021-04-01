from simulation.model.place import Place


class Warehouse(Place):

    id = 0

    def __init__(self, location, products):
        super().__init__(location)

        self.id = Warehouse.id

        Warehouse.id += 1

        self.products = products

    def product(self, product_type):
        product = None

        for p in self.products:
            if p.type == product_type:
                return p

        return product

    def decrease_product(self, product_type):
        self.products.remove(self.product(product_type))

    def increase_product(self, product):
        self.products.append(product)

    def __eq__(self, other):
        return self.id == other.id

    def __str__(self):
        return f'w{self.id}'

    def __repr__(self):
        return self.__str__()