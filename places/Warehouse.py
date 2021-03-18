from Place import Place

class Warehouse(Place):
    def __init__(self, x, y):
        Place.__init__(self, x, y) 
        # Items stored in the warehouse
        self.items = {}

    def addItem(self, id, quantity):
        self.items[id] += quantity

    def removeItem(self, id, quantity):
        if self.items[id] < quantity:
            return False;
        self.items[id] -= quantity
        return True