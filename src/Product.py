class Product:
    def __init__(self, product, lastPlace):
        self.productType = product
        self.lastPlace = lastPlace
        self.orderPlace = None

    def assignOrder(self, client):
        self.orderPlace = client

    def isFinished(self):
        return self.lastPlace == self.orderPlace

    def __str__(self):
        return "Product of type " + str(self.productType) + ("sent to" if self.isFinished() else " stored in") + " the " + str(self.lastPlace)
