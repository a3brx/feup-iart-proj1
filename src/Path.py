class Path:
    def __init__(self, product, destination=None):
        self.product = product
        self.drone = None
        self.destination = destination if destination != None else product.orderPlace

    def assignDrone(self, drone):
        self.drone = drone

    def __str__(self):
        return "Path of product " + str(self.product.productType) + " to " + self.destination.getStringLocation() + " made by drone " + str(self.drone)