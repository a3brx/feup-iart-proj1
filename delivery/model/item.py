class Product:
    def __init__(self, product_id, weight):
        self.id = product_id
        self.weight = weight

    def __str__(self):
        return "p" + str(self.id)


class Item:
    def __init__(self, item_id, product, origin):
        self.id = item_id
        self.product = product
        self.origin = origin

    def __str__(self):
        return "i" + str(self.id) + " of " + str(self.product)
