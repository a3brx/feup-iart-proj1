from math import sqrt, ceil
from collections import OrderedDict

from Product import *

calculatedDistances = {}

class Place:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, operand):
        diffx = abs(self.x - operand.x)
        diffy = abs(self.y - operand.y)
        if diffy < diffx:
            tupleKey = (diffy, diffx)
        else:
            tupleKey = (diffx, diffy)
        if tupleKey in calculatedDistances.keys():
            return calculatedDistances[tupleKey]
        else:
            value = ceil(sqrt(diffx * diffx + diffy * diffy))
            calculatedDistances[tupleKey] = value
            return value

    def distanceToProduct(self, product):
        return self.distanceTo(product.lastPlace)

    def getStringLocation(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Warehouse(Place):
    def __init__(self, warehouseId, coordinates, items):
        super().__init__(*map(int, coordinates))
        self.id = warehouseId
        self.createProducts(map(int, items))

    def createProducts(self, itemQuantities):
        self.products = []
        for productType, productquantity in enumerate(itemQuantities):
            productsOfType = [self.createProduct(productType) for _ in range(productquantity)]
            self.products.extend(productsOfType)

    def createProduct(self, productType):
        return Product(int(productType), self)

    def __str__(self):
        return "Warehouse at " + self.getStringLocation()


class Client(Place):
    def __init__(self, clientId, coordinates, products):
        super().__init__(*map(int, coordinates))
        self.id = clientId
        self.wantedProducts = list(map(int, products))

    def __str__(self):
        return "Client at " + self.getStringLocation()

    def __len__(self):
        return len(self.wantedProducts)
