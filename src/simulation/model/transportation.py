class Transportation:

    def __init__(self, product_type, drone, source, destination):
        """Instantiates a transportation

        ...
        Args:
            product_type (integer): The product type to be moved
            drone (integer): The drone assigned to the product
            source (Warehouse): The place where the product comes from
            destination (Place): The place to be delivered
        """

        self.product_type = product_type
        self.drone = drone
        self.source = source
        self.destination = destination
