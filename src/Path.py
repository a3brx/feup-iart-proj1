class Path:
    def __init__(self, product, destination=None):
        self.product = product
        self.drone = None
        self.destination = destination if destination != None else product.orderPlace

    def assignDrone(self, drone):
        self.drone = drone

    def duration(self):
        return self.product.distanceTo(self.destination) + 2

    def __str__(self):
        return "Path of product " + str(self.product.productType) + " to " + self.destination.getStringLocation() + " made by drone " + str(self.drone)

    def getOutputString(self):
        beginning = str(self.drone) + " "
        middle = "D" if self.destination == self.product.orderPlace else "U"
        end = " " + str(self.destination.id) + " " + str(self.product.productType) + " 1\n"
        return beginning + "L" + end + beginning + middle + end