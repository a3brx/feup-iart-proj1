class Transportation:

    def __init__(self, product, drone, source, destination):
        """Instantiates a transportation

        ...
        Args:
            product (Product): The product to be moved
            drone (integer): The drone assigned to the product
            source (Warehouse): The place where the product comes from
            destination (Place): The place to be delivered
        """

        self.product = product
        self.drone = drone
        self.source = source
        self.destination = destination

    def __str__(self):
        return f'{self.product} with drone {self.drone} to {self.destination}'

    def __repr__(self):
        return self.__str__()
