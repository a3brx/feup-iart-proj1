class Command:

    def __init__(self, drone_id, command, warehouse_id=0, product_type=0, number_of_items=0, customer_id=0, number_of_turns=0):
        self.drone_id = drone_id
        self.command = command
        self.warehouse_id = warehouse_id
        self.product_type = product_type
        self.number_of_items = number_of_items
        self.customer_id = customer_id
        self.number_of_turns = number_of_turns

    @classmethod
    def from_string(cls, string):
        drone, command, place, product_type, number_of_items = string.split(
            ' ')

        drone = int(drone)
        place = int(place)
        product_type = int(product_type)
        number_of_items = int(number_of_items)

        if command == 'L':
            return cls(drone, command, place, product_type, number_of_items)
        else:
            return cls(drone, command, customer_id=place, product_type=product_type, number_of_items=number_of_items)

    def __str__(self):
        if self.command == 'L' or self.command == 'U':
            return f'{self.drone_id} {self.command} {self.warehouse_id} {self.product_type} {self.number_of_items}'
        if self.command == 'D':
            return f'{self.drone_id} {self.command} {self.customer_id} {self.product_type} {self.number_of_items}'

        return f'{self.drone_id} {self.command} {self.number_of_turns}'

    def __repr__(self):
        return self.__str__()
