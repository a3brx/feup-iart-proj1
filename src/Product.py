class Product:
    def __init__(self, product, lastPlace):
        self.productType = product
        self.lastPlace = lastPlace
        self.orderPlace = None

    def assignOrder(self, client):
        self.orderPlace = client

    def isFinished(self):
        return self.lastPlace == self.orderPlace

    def distanceTo(self, place):
        return self.lastPlace.distanceTo(place)

    def __str__(self):
        resultString = "Product of type " + str(self.productType)
        if self.isFinished():
            resultString += " sent to "
        elif self.orderPlace is not None:
            resultString += " to be send to a " + str(self.orderPlace) + " stored in the "
        else:
            resultString += " stored in the "
        return resultString + str(self.lastPlace)
