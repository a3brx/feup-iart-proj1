class Path:
    def __init__(self, product, destination=None):
        self.product = product
        self.drone = None
        self.destination = destination if destination != None else product.order_place

    def assign_drone(self, drone):
        self.drone = drone

    def duration(self):
        return self.product.distance_to(self.destination) + 2

    def __str__(self):
        return "Path of product " + str(self.product.product_type) + " to " + self.destination.get_string_location() + " made by drone " + str(self.drone)

    def get_output_string(self):
        beginning = str(self.drone) + " "
        middle = "D" if self.destination == self.product.order_place else "U"
        end = " " + str(self.destination.id) + " " + \
            str(self.product.product_type) + " 1\n"
        return beginning + "L" + end + beginning + middle + end
