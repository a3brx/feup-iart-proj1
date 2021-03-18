from Place import Place

class Client(Place):

    def __init__(self, x, y, quantity):
        Place.__init__(self, x, y) 
        # Number or items to be send to the client
        self.order = quantity

    def send(self, quantity):
        self.order -= quantity

    def isDone(self):
        return self.numberOfItems <= 0