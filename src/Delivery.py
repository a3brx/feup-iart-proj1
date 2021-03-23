from Place import *

# Immutable data shared between all delivery solutions


class Data:
    def __init__(self, rows, columns, drones, turns, payload, weights):
        self.numberOfRows = rows
        self.numberOfColumns = columns
        self.numberOfDrones = drones
        self.numberOfTurns = turns
        self.maxPayload = payload
        self.productWeights = tuple(map(int, weights))


class Delivery:
    def __init__(self, rows, columns, drones, turns, payload, weights, warehouses, clients):
        self.data = Data(rows, columns, drones, turns, payload, weights)
        self.warehouses = warehouses
        self.clients = clients
        self.products = [
            product for warehouse in warehouses for product in warehouse.products
        ]
        self.solution = self.getInitialSolution()

    def getInitialSolution(self):
        productsNotAssigned = self.products
        ordersSortedBySize = sorted(self.clients, key=len)
        for order in ordersSortedBySize:
            productsNotAssigned = sorted(
                productsNotAssigned, key=order.distanceToProduct
            )
            for productType in order.wantedProducts:
                productToAssign = next(
                    index for index, product in enumerate(productsNotAssigned) if product.productType == productType
                )
                productsNotAssigned.pop(productToAssign).assignOrder(order)

    @classmethod
    def fromInputFile(cls, file):
        with open("data/" + file + ".in") as inputFile:
            # Problem
            problemInformation = inputFile.readline().split()
            numberOfProducts = inputFile.readline()
            productWeights = inputFile.readline().split()

            # Warehouses
            numberOfWarehouses = int(inputFile.readline())
            warehouses = []
            for i in range(numberOfWarehouses):
                warehouseCoordinates = inputFile.readline().split()
                warehouseItems = inputFile.readline().split()
                warehouses.append(
                    Warehouse(warehouseCoordinates, warehouseItems))

            # Orders
            numberOfOrders = int(inputFile.readline())
            clients = []
            for i in range(numberOfOrders):
                orderCoordinates = inputFile.readline().split()
                orderNumberOfItems = inputFile.readline()
                orderProducts = inputFile.readline().split()
                clients.append(Client(orderCoordinates, orderProducts))

            return Delivery(*problemInformation, productWeights, warehouses, clients)
