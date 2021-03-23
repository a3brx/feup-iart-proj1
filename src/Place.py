from math import sqrt

from Product import *


class Place:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, operand):
        return sqrt(pow(self.x - operand.x, 2) + pow(self.y - operand.y, 2))

    def getStringLocation(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Warehouse(Place):
    def __init__(self, coordinates, items):
        super().__init__(*map(int, coordinates))
        self.products = list(map(self.createProduct, items))

    def createProduct(self, productType):
        return Product(int(productType), self)

    def __str__(self):
        return "Warehouse at " + self.getStringLocation()


class Client(Place):
    def __init__(self, coordinates, products):
        super().__init__(*map(int, coordinates))
        self.productsWanted = list(map(int, products))
        print(self.productsWanted)

    def __str__(self):
        return "Client at " + self.getStringLocation()
