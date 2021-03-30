class Product:

    id = 0

    def __init__(self, type, weight):
        self.id = Product.id

        Product.id += 1

        self.type = type
        self.weight = weight

    def __str__(self):
        return f'p{self.id} of type {self.type}'

    def __repr__(self):
        return self.__str__()
