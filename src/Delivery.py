from Place import *
from Path import *
from random import randrange


class Data:
    def __init__(self, rows, columns, drones, turns, payload, weights):
        self.numberOfRows = int(rows)
        self.numberOfColumns = int(columns)
        self.numberOfDrones = int(drones)
        self.numberOfTurns = int(turns)
        self.maxPayload = int(payload)
        self.productWeights = tuple(map(int, weights))


class Delivery:
    def __init__(self, rows, columns, drones, turns, payload, weights, warehouses, clients):
        self.data = Data(rows, columns, drones, turns, payload, weights)
        self.warehouses = warehouses
        self.clients = clients
        self.products = [
            product for warehouse in warehouses for product in warehouse.products
        ]
        self.solution = self.initialSolution()

    def initialSolution(self):
        def assignProducts():
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

        def assignDrones(solution):
            for path in solution:
                path.assignDrone(randrange(self.data.numberOfDrones))

        assignProducts()
        solution = list(map(Path, filter(lambda x: x.hasOrder(), self.products)))
        assignDrones(solution)
        return solution

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
