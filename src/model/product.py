class Product:
    def __init__(self, product, last_place):
        self.product_type = product
        self.last_place = last_place
        self.order_place = None

    def assign_order(self, client):
        self.order_place = client

    def has_order(self):
        return self.order_place != None

    def is_finished(self):
        return self.last_place == self.order_place

    def distance_to(self, place):
        return self.last_place.distance_to(place)

    def __str__(self):
        result_string = "Product of type " + str(self.product_type)
        if self.is_finished():
            result_string += " sent to "
        elif self.order_place is not None:
            result_string += " to be send to a " + str(self.order_place) + " stored in the "
        else:
            result_string += " stored in the "
        return result_string + str(self.last_place)
