from model.place import Client


class Path:
    def __init__(self, product, destination=None, drone=None):
        self.product = product
        self.destination = destination if destination != None else product.order_place
        self.drone = drone

    def copy(self):
        return Path(self.product.copy(), self.destination, self.drone)

    def assign_drone(self, drone):
        self.drone = drone

    def duration(self):
        return self.product.distance_to(self.destination) + 2

    def is_final(self):
        return isinstance(self.destination, Client)

    def __str__(self):
        return "Path of product " + str(id(self.product)) + " to " + str(self.destination) + " made by drone " + str(self.drone)

    def get_output_string(self):
        beginning = str(self.drone) + " "
        middle = "D" if self.destination == self.product.order_place else "U"
        end = " " + str(self.destination.id) + " " + \
            str(self.product.product_type) + " 1\n"
        return beginning + "L" + end + beginning + middle + end
