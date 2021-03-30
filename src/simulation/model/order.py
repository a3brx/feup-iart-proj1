from simulation.model.place import Place


class Order(Place):

    def __init__(self, location, product_types):
        super().__init__(location)
        self.product_types = product_types
