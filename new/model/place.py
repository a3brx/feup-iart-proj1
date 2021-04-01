from math import ceil, sqrt


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def distance_to(self, operand):
        return ceil(sqrt((self.x - operand.x) ** 2 + (self.y - operand.y) ** 2))

    def __eq__(self, operand):
        return self.x == operand.x and self.y == operand.y


class Place:
    def __init__(self, place_id, x, y):
        self.position = Position(x, y)
        self.id = place_id

    def __str__(self):
        return str(self.id) + " at " + str(self.position)

    def copy(self):
        return self

    def distance_to(self, operand):
        return self.position.distance_to(operand.position)


class Client(Place):
    def __init__(self, client_id, x, y, order):
        super().__init__(client_id, x, y)
        self.initial_order = order.copy()
        self.order = order.copy()

    def __str__(self):
        return "cl" + super().__str__()

    def __len__(self):
        return len(self.order)
    
    def copy(self):
        return Client(self.id, self.position.x, self.position.y, self.initial_order)


class Warehouse(Place):
    def __init__(self, warehouse_id, x, y):
        super().__init__(warehouse_id, x, y)

    def __str__(self):
        return "wr" + super().__str__()

    def copy(self):
        return self
